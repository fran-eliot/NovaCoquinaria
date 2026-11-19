"""RET-D03: candidatos de preparación y presentación, aislados del extractor."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

from common import ROOT_DIR
from extract_recipe_metadata import build_projection, serialize, snapshot_bytes, read_metadata
from build_recipe_index import build_index
from experiment_retrieval_text import occurrence
from ingredient_identity_candidates import key

FIXTURE = ROOT_DIR / "tools/fixtures/retrieval_identity_cases.json"


def compile_rules(rules):
    labels = defaultdict(list)
    for rule in rules:
        for label in rule["labels"]:
            labels[key(label)].append({"ingredient_id": rule["ingredient_id"],
                                      "rule": rule["id"]})
    return dict(labels)


def propose(entry, rules):
    # Do not extend existing candidates, override explicit links or repair ambiguity.
    if (entry["resolution"] != "unresolved" or entry["identity_candidates"]
            or not entry["name"]):
        return []
    # Exact reviewed labels only; preserve accents via the existing candidate key
    # semantics (accent folding), never discard internal conjunctions or qualifiers.
    label = key(entry["name"])
    # A reviewed comma after the first noun may introduce a preparation qualifier.
    # No arbitrary punctuation stripping or truncation.
    label = label.replace("ajo, ", "ajo ", 1) if label.startswith("ajo, ") else label
    return sorted(rules.get(label, []), key=lambda m: (m["ingredient_id"], m["rule"]))


def evaluate(index, fixture):
    if (index["source_commit"], index["extractor_version"], index["index_version"]) != (
            fixture["source_commit"], fixture["extractor_version"], fixture["index_version"]):
        raise ValueError("Corpus o versión incompatible")
    compiled = compile_rules(fixture["rules"])
    additions = []
    baseline = Counter()
    by_rule = defaultdict(set)
    by_ingredient = defaultdict(set)
    by_recipe = set()
    for identity, record in sorted(index["records"].items()):
        for pos, entry in enumerate(record["ingredients"]):
            baseline["occurrences"] += 1
            if entry["resolution"] == "explicit":
                baseline["explicit"] += 1
            elif entry["identity_candidates"]:
                baseline["existing_candidates"] += 1
            else:
                baseline["without_candidate_or_identity"] += 1
            new = propose(entry, compiled)
            if new:
                ref = (identity, pos)
                additions.append({**occurrence(index, ref), "proposed": new})
                by_recipe.add(identity)
                for match in new:
                    by_rule[match["rule"]].add(ref)
                    by_ingredient[match["ingredient_id"]].add(ref)
    cases = []
    for case in fixture["cases"]:
        ref = (case["recipe_id"], case["position"])
        entry = index["records"][ref[0]]["ingredients"][ref[1]]
        if entry["name"] != case["name"]:
            raise ValueError("Muestra incompatible: " + case["id"])
        observed = propose(entry, compiled)
        cases.append({"id": case["id"], "expected": case["expected"],
                      "observed": observed, "passed": observed == case["expected"],
                      "occurrence": occurrence(index, ref),
                      "existing_candidates": entry["identity_candidates"]})
    negatives = [{"name": name, "proposed": propose({"name": name,
                  "resolution": "unresolved", "identity_candidates": []}, compiled)}
                 for name in fixture["synthetic_negative"]]
    return {"stage": "retrieval_identity_experiment",
            "source_commit": index["source_commit"],
            "projection_sha256": index["projection_sha256"],
            "baseline": dict(baseline), "added_occurrences": len(additions),
            "added_recipes": len(by_recipe),
            "remaining_without_candidate_or_identity":
                baseline["without_candidate_or_identity"] - len(additions),
            "by_rule": {k: len(v) for k, v in sorted(by_rule.items())},
            "by_ingredient": {k: len(v) for k, v in sorted(by_ingredient.items())},
            "cases": cases, "passed_cases": sum(c["passed"] for c in cases),
            "case_count": len(cases), "synthetic_negative": negatives,
            "negative_passed": sum(not n["proposed"] for n in negatives),
            "additions": additions, "scope": "Propuestas experimentales, no resolución"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()):
        parser.error("Salida derivada bajo site/")
    raw = FIXTURE.read_bytes()
    fixture = json.loads(raw)
    commit = fixture["source_commit"]
    for rule in fixture["rules"]:
        fields, _ = read_metadata(snapshot_bytes(ROOT_DIR, commit, rule["path"]), rule["path"])
        if not fields or fields.get("tipo") != "ingrediente" or fields.get("id") != rule["ingredient_id"]:
            raise ValueError("Ficha de ingrediente incompatible: " + rule["id"])
    projection = serialize(build_projection(ROOT_DIR, commit)).encode("utf-8")
    report = evaluate(build_index(projection), fixture)
    report["fixture_sha256"] = hashlib.sha256(raw).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in
                      ("cases", "synthetic_negative", "additions")}, ensure_ascii=False, sort_keys=True))
    if (report["passed_cases"] != report["case_count"]
            or report["negative_passed"] != len(report["synthetic_negative"])):
        parser.exit(1, "Expectativas de candidatos incumplidas\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
