"""CCE-D04B: isolated compatibility experiment; no production query changes."""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from common import ROOT_DIR
from build_recipe_index import build_index, text_key, digest
from extract_recipe_metadata import build_projection, serialize
from recipe_ingredient_index import build_ingredient_indexes

OPTIONS = ("required", "optional", "unknown")
STATES = ("available", "unavailable", "unknown")
FIXTURE = ROOT_DIR / "tools/fixtures/compatibility_experiment_cases.json"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def literal(value):
    return isinstance(value, str) and bool(value) and value == value.strip()


def items(values, universe=None, normalize=lambda x: x):
    require(isinstance(values, list) and all(literal(v) for v in values), "Invalid list")
    result = {normalize(v) for v in values}
    require(len(result) == len(values), "Duplicate list items")
    require(universe is None or result <= universe, "Unknown ID")
    return result


def evaluate(index, declaration, selection=None, modality="A"):
    require(isinstance(index, dict) and
            (index.get("index_version"), index.get("stage")) ==
            ("0.2.0", "recipe_index_ingredients_preview") and
            digest(index.get("source_commit"), 40) and
            digest(index.get("projection_sha256"), 64), "Invalid index")
    require(modality in ("A", "B", "C"), "Invalid modality")
    records = index["records"]
    require(isinstance(records, dict), "Invalid records")
    for rid, record in records.items():
        require(literal(rid) and record["id"] == rid and
                record["source"]["commit"] == index["source_commit"] and
                digest(record["source"]["sha256"], 64) and literal(record["source"]["path"]) and
                literal(record["title"]) and isinstance(record["ingredients"], list), "Invalid record")
        for entry in record["ingredients"]:
            require(isinstance(entry.get("quantity"), dict), "Invalid quantity")
    postings, _ = build_ingredient_indexes(records, text_key)
    require(postings == index["ingredients"], "Inconsistent postings")
    universe = set(postings["by_explicit_id"]) | set(postings["by_candidate_id"])
    selected = set(records) if selection is None else items(selection, set(records))
    require(isinstance(declaration, dict) and set(declaration) <=
            {"mode", "present_ids", "absent_ids", "present_labels", "atomic", "presentation", "source_commit"},
            "Invalid declaration")
    mode = declaration.get("mode", "open")
    require(mode in ("open", "closed"), "Invalid inventory mode")
    present = items(declaration.get("present_ids", []), universe)
    absent = items(declaration.get("absent_ids", []), universe)
    labels = items(declaration.get("present_labels", []), normalize=text_key)
    require(not present & absent, "Contradictory inventory")

    def reviewed(field):
        values = declaration.get(field, [])
        require(isinstance(values, list), "Invalid confirmation list")
        require(not values or declaration.get("source_commit") == index["source_commit"],
                "Confirmation corpus mismatch")
        result = set()
        for value in values:
            require(isinstance(value, list) and len(value) == 3, "Invalid confirmation")
            rid, pos, iid = value
            require(literal(rid) and rid in selected and type(pos) is int and
                    0 <= pos < len(records[rid]["ingredients"]) and literal(iid), "Invalid reference")
            entry = records[rid]["ingredients"][pos]
            require(entry["resolution"] == "explicit" and entry["ingredient_id"] == iid,
                    "Invalid explicit identity")
            require(tuple(value) not in result, "Duplicate confirmation")
            result.add(tuple(value))
        return result

    atomic, presentation = reviewed("atomic"), reviewed("presentation")
    require(all(iid in present for _, _, iid in presentation), "Presentation without presence")
    require(declaration.get("source_commit", index["source_commit"]) == index["source_commit"],
            "Declaration corpus mismatch")
    results = []
    for rid in sorted(selected):
        record = records[rid]
        matrix = {o: {state: 0 for state in STATES} for o in OPTIONS}
        occurrences = []
        for pos, entry in enumerate(record["ingredients"]):
            iid = entry["ingredient_id"]
            ref = (rid, pos, iid)
            state = "unknown"
            if entry["resolution"] != "explicit":
                reason = "identity_not_explicit"
            elif ref not in atomic:
                reason = "atomicity_unknown"
            elif iid in present:
                if ref in presentation:
                    state, reason = "available", "present_presentation_confirmed"
                else:
                    reason = "presentation_unknown"
            elif iid in absent:
                state, reason = "unavailable", "explicitly_absent"
            elif mode == "closed":
                state, reason = "unavailable", "closed_absent"
            else:
                reason = "open_unspecified"
            hints = []
            if modality == "B":
                hints = [deepcopy(m) for m in entry["identity_candidates"] if m["ingredient_id"] in present]
            if modality == "C" and entry["name"] and text_key(entry["name"]) in labels:
                hints = [{"label": text_key(entry["name"])}]
            matrix[entry["optionality"]][state] += 1
            occurrences.append({**deepcopy(entry), "position": pos, "availability": state,
                                "reason": reason, "atomic_confirmed": ref in atomic,
                                "presentation_confirmed": ref in presentation,
                                "quantity_evaluated": False, "hints": hints})
        required = matrix["required"]
        classification = ("required_missing" if required["unavailable"] else
                          "indeterminate" if required["unknown"] or not sum(required.values())
                          or sum(matrix["unknown"].values()) else "required_presence_confirmed")
        results.append({"id": rid, "title": record["title"], "source": deepcopy(record["source"]),
                        "classification": classification, "matrix": matrix, "occurrences": occurrences})
    return {"stage": "compatibility_experiment", "experiment_version": "0.1.0",
            "source_commit": index["source_commit"], "projection_sha256": index["projection_sha256"],
            "modality": modality, "selection": sorted(selected),
            "declaration": {"mode": mode, "present_ids": sorted(present), "absent_ids": sorted(absent),
                            "present_labels": sorted(labels), "atomic": sorted(atomic),
                            "presentation": sorted(presentation), "source_commit": index["source_commit"]},
            "results": results}


def reference(index, declaration, selection):
    """Direct traversal; independent state sets and aggregation, not postings."""
    present, absent = set(declaration.get("present_ids", [])), set(declaration.get("absent_ids", []))
    atomic = {tuple(x) for x in declaration.get("atomic", [])}
    presentation = {tuple(x) for x in declaration.get("presentation", [])}
    expected = {}
    for rid in sorted(index["records"] if selection is None else selection):
        entries = index["records"][rid]["ingredients"]
        eligible = {(rid, i, e["ingredient_id"]) for i, e in enumerate(entries)
                    if e["resolution"] == "explicit"} & atomic
        positive = {ref[1] for ref in eligible & presentation if ref[2] in present}
        negative = {ref[1] for ref in eligible if ref[2] in absent or
                    (declaration.get("mode") == "closed" and ref[2] not in present)}
        states = ["available" if i in positive else "unavailable" if i in negative else "unknown"
                  for i in range(len(entries))]
        required = [states[i] for i, e in enumerate(entries) if e["optionality"] == "required"]
        classification = "required_missing" if "unavailable" in required else (
            "required_presence_confirmed" if required and set(required) == {"available"}
            and all(e["optionality"] != "unknown" for e in entries) else "indeterminate")
        expected[rid] = (states, classification)
    return expected


def contrast(index, declaration, selection):
    runs = [evaluate(index, declaration, selection, m) for m in ("A", "B", "C")]
    expected = reference(index, declaration, selection)
    summary = {}
    for run in runs:
        observed = {r["id"]: ([e["availability"] for e in r["occurrences"]], r["classification"])
                    for r in run["results"]}
        require(observed == expected, "Reference discrepancy")
        require(run == evaluate(index, declaration, selection, run["modality"]), "Non-deterministic result")
        counts = Counter(e["availability"] for r in run["results"] for e in r["occurrences"])
        require(all(sum(sum(row.values()) for row in r["matrix"].values()) == len(r["occurrences"])
                    for r in run["results"]), "Matrix discrepancy")
        summary[run["modality"]] = {"recipes": len(run["results"]), "occurrences": sum(counts.values()),
                                    "availability": {k: counts[k] for k in STATES},
                                    "classifications": dict(Counter(r["classification"] for r in run["results"])),
                                    "hint_occurrences": sum(bool(e["hints"]) for r in run["results"] for e in r["occurrences"])}
    return runs, summary


def experiment(index, fixture):
    require(index["source_commit"] == fixture["source_commit"] and
            index["projection_sha256"] == fixture["projection_sha256"], "Fixture corpus mismatch")
    rid = fixture["recipe_id"]
    require(index["records"][rid]["source"]["path"] == fixture["path"], "Fixture path mismatch")
    atomic = [[rid, pos, iid] for pos, iid in fixture["atomic"]]
    reports = []
    for case in fixture["cases"]:
        declaration = {"mode": case["mode"], "present_ids": case["present_ids"],
                       "absent_ids": case["absent_ids"], "atomic": atomic,
                       "source_commit": index["source_commit"],
                       "presentation": [a for a in atomic if a[1] in case["presentation"]]}
        runs, summary = contrast(index, declaration, [rid])
        result = runs[0]["results"][0]
        observed = {p: result["occurrences"][int(p)]["availability"] for p in case["expected"]}
        require(observed == case["expected"] and result["classification"] == case["classification"],
                "Documentary case failed: " + case["id"])
        reports.append({"id": case["id"], "expected": case["expected"], "observed": observed,
                        "classification": result["classification"], "summary": summary, "results": runs})
    for case in fixture["additional"]:
        rid = case["recipe_id"]
        require(index["records"][rid]["source"]["path"] == case["path"], "Fixture path mismatch")
        declaration = {"present_ids": [case["candidate"]] if "candidate" in case else [],
                       "present_labels": [case["label"]]}
        runs, summary = contrast(index, declaration, [rid])
        entries = [run["results"][0]["occurrences"][case["position"]] for run in runs]
        require(all(e["availability"] == case["expected"] for e in entries), "Additional state mismatch")
        require(bool(entries[1]["hints"]) == ("candidate" in case) and bool(entries[2]["hints"]),
                "Additional hint mismatch: " + rid)
        reports.append({"id": rid, "summary": summary, "results": runs})
    # Full corpus, no manual confirmations: establish the abstention baseline.
    _, baseline = contrast(index, {"mode": "closed", "present_ids": ["ING-0012"],
                                  "present_labels": ["leche de coco", "leche de coco;"]}, None)
    return {"source_commit": index["source_commit"], "projection_sha256": index["projection_sha256"],
            "cases": reports, "case_count": len(reports), "baseline": baseline,
            "scope": "Directed documentary cases and consistency; not culinary accuracy"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    require(output.is_relative_to((ROOT_DIR / "site").resolve()), "Output must be under site/")
    raw = FIXTURE.read_bytes()
    fixture = json.loads(raw)
    index = build_index(serialize(build_projection(ROOT_DIR, fixture["source_commit"])).encode("utf-8"))
    report = experiment(index, fixture)
    report["fixture_sha256"] = hashlib.sha256(raw).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n",
                      encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, sort_keys=True))


if __name__ == "__main__":
    main()
