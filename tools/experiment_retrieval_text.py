"""RET-D02: experimento aislado sobre el corpus fijado en RET-D01."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata

from common import ROOT_DIR
from extract_recipe_metadata import build_projection, serialize
from build_recipe_index import build_index, text_key

MODES = ("exact", "terms", "folded")
FIXTURE = ROOT_DIR / "tools/fixtures/retrieval_baseline_cases.json"
QUERIES = ("ajo", "salsa de soja", "leche", "leche de coco", "aceite",
           "sal", "huevo", "huevos", "azucar", "azúcar", "limon", "limón",
           "cafe", "café", "pollo", "vinagre de vino", "harina de maíz")


def tokens(value, folded=False):
    value = text_key(value)
    if folded:
        value = "".join(c for c in unicodedata.normalize("NFD", value)
                        if not unicodedata.combining(c))
    return tuple(re.findall(r"[^\W_]+", value, flags=re.UNICODE))


def contains_terms(haystack, needle):
    return bool(needle) and any(haystack[i:i + len(needle)] == needle
                                for i in range(len(haystack) - len(needle) + 1))


def retrieve(index, query, mode):
    if mode not in MODES:
        raise ValueError("Modalidad desconocida")
    if not isinstance(query, str) or not text_key(query) or not tokens(query):
        raise ValueError("Consulta sin términos")
    by_text = index["ingredients"]["by_text"]
    if mode == "exact":
        keys = [text_key(query)] if text_key(query) in by_text else []
    else:
        folded = mode == "folded"
        needle = tokens(query, folded)
        keys = [key for key in by_text if contains_terms(tokens(key, folded), needle)]
    return {(p["recipe_id"], p["position"]) for key in keys for p in by_text[key]}


def occurrence(index, ref):
    identity, position = ref
    record = index["records"][identity]
    entry = record["ingredients"][position]
    return {"recipe_id": identity, "position": position, "path": record["source"]["path"],
            "source_location": entry["source_location"], "name": entry["name"],
            "raw": entry["raw"], "optionality": entry["optionality"],
            "resolution": entry["resolution"], "ingredient_id": entry["ingredient_id"]}


def summarize(index, query, mode, hits, previous):
    new = hits - previous
    return {"mode": mode, "occurrences": len(hits),
            "recipes": len({r[0] for r in hits}),
            "added_occurrences": len(new),
            "added_recipes": len({r[0] for r in hits} - {r[0] for r in previous}),
            "removed_occurrences": len(previous - hits),
            "added": [occurrence(index, ref) for ref in sorted(new)],
            "removed": [occurrence(index, ref) for ref in sorted(previous - hits)]}


def evaluate(index, fixture):
    if (index["source_commit"], index["extractor_version"], index["index_version"]) != (
            fixture["source_commit"], fixture["extractor_version"], fixture["index_version"]):
        raise ValueError("Corpus o versión incompatible")
    queries = sorted(set(QUERIES) | {c["query"] for c in fixture["cases"]})
    hits = {q: {mode: retrieve(index, q, mode) for mode in MODES} for q in queries}
    outcomes = []
    for case in fixture["cases"]:
        ref = (case["recipe_id"], case["position"])
        original = occurrence(index, ref)
        if (original["path"] != case["path"] or original["name"] != case["name"]
                or original["source_location"]["start_line"] != case["line"]):
            raise ValueError("Muestra incompatible: " + case["id"])
        observed = {mode: ref in hits[case["query"]][mode] for mode in MODES}
        outcomes.append({"id": case["id"], "query": case["query"],
                         "feature": case["feature"], "expected": case["expected"],
                         "observed": observed, "passed": observed == case["expected"],
                         "occurrence": original})
    reports = []
    for q in queries:
        exact, terms, folded = (hits[q][mode] for mode in MODES)
        reports.append({"query": q, "modalities": [
            summarize(index, q, "exact", exact, set()),
            summarize(index, q, "terms", terms, exact),
            summarize(index, q, "folded", folded, terms)]})
    return {"stage": "retrieval_text_experiment", "source_commit": index["source_commit"],
            "extractor_version": index["extractor_version"], "index_version": index["index_version"],
            "projection_sha256": index["projection_sha256"],
            "inventory": index["inventory"], "cases": outcomes,
            "passed_cases": sum(c["passed"] for c in outcomes), "case_count": len(outcomes),
            "queries": reports, "scope": "Menciones textuales; no identidad ni precisión estimada"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()):
        parser.error("Salida derivada bajo site/")
    fixture_raw = FIXTURE.read_bytes()
    fixture = json.loads(fixture_raw)
    projection = serialize(build_projection(ROOT_DIR, fixture["source_commit"])).encode("utf-8")
    report = evaluate(build_index(projection), fixture)
    report["fixture_sha256"] = hashlib.sha256(fixture_raw).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
                      encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("source_commit", "projection_sha256",
          "case_count", "passed_cases")}, ensure_ascii=False))
    for item in report["queries"]:
        print(json.dumps({"query": item["query"], "modalities": [
            {k: v for k, v in m.items() if k not in ("added", "removed")}
            for m in item["modalities"]]}, ensure_ascii=False, sort_keys=True))
    if report["passed_cases"] != report["case_count"]:
        parser.exit(1, "Expectativas de recuperación incumplidas\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
