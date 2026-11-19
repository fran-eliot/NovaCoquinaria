"""Unidad C: contraste de integración, regresión y evidencia del modo terms."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata

from common import ROOT_DIR
from build_recipe_index import build_index
from extract_recipe_metadata import build_projection, serialize
from experiment_retrieval_text import FIXTURE, QUERIES, retrieve
from evaluate_recipe_queries import evaluate as evaluate_legacy
from query_recipe_index import query, QUERY_VERSION


def require(condition, message):
    if not condition:
        raise ValueError(message)


def words(value):
    # Oráculo independiente de los postings y del núcleo léxico compartido.
    return re.findall(r"[^\W_]+", unicodedata.normalize("NFC", value.casefold()))


def scan(index, value, mode):
    result = set()
    needle = words(value)
    for identity, record in index["records"].items():
        for pos, entry in enumerate(record["ingredients"]):
            name = entry["name"]
            if not name:
                continue
            if mode == "text":
                canonical = lambda s: unicodedata.normalize("NFC", " ".join(s.casefold().split()))
                matched = canonical(name) == canonical(value)
            else:
                parts = words(name)
                matched = bool(needle) and any(parts[i:i+len(needle)] == needle
                    for i in range(len(parts)-len(needle)+1))
            if matched:
                result.add((identity, pos))
    return result


def observed_refs(index, value, mode):
    clauses = [{"mode": mode, "value": value}]
    result = query(index, ingredients=clauses)
    require(result == query(index, ingredients=clauses), "Resultado no determinista")
    ids = [row["id"] for row in result["results"]]
    require(ids == sorted(set(ids)) and result["count"] == len(ids), "IDs inconsistentes")
    require(result["source_commit"] == index["source_commit"] and
            result["projection_sha256"] == index["projection_sha256"], "Procedencia incorrecta")
    refs = set()
    for row in result["results"]:
        record = index["records"][row["id"]]
        require(row["source"] == {k: record["source"][k] for k in
                ("commit", "path", "sha256")}, "Fuente incorrecta")
        reason, = row["matches"]
        require(reason["mode"] == mode and reason["value"] == value, "Motivo incorrecto")
        require((reason.get("match_scope") == "textual_mention") == (mode == "terms"),
                "Alcance incorrecto")
        positions = [entry["position"] for entry in reason["occurrences"]]
        require(positions == sorted(set(positions)), "Posiciones duplicadas o desordenadas")
        for entry in reason["occurrences"]:
            original = record["ingredients"][entry["position"]]
            require(all(entry[key] == original[key] for key in
                ("raw", "name", "optionality", "resolution", "ingredient_id", "source_location")),
                "Evidencia alterada")
            refs.add((row["id"], entry["position"]))
    return refs


def evaluate(index, fixture=None):
    reports = []
    all_refs = {}
    for value in QUERIES:
        counts = {}
        for mode in ("text", "terms"):
            actual = observed_refs(index, value, mode)
            require(actual == scan(index, value, mode), f"Oráculo discrepante: {mode} {value}")
            if fixture is not None:
                expected = retrieve(index, value, "exact" if mode == "text" else mode)
                require(actual == expected, f"Experimento discrepante: {mode} {value}")
            all_refs[value, mode] = actual
            counts[mode] = {"occurrences": len(actual), "recipes": len({r[0] for r in actual})}
        reports.append({"query": value, "counts": counts})
    cases = []
    if fixture is not None:
        require(index["source_commit"] == fixture["source_commit"], "Corte incorrecto")
        for case in fixture["cases"]:
            ref = case["recipe_id"], case["position"]
            record = index["records"][ref[0]]
            entry = record["ingredients"][ref[1]]
            require(record["source"]["path"] == case["path"] and entry["name"] == case["name"]
                    and entry["source_location"]["start_line"] == case["line"], "Muestra alterada")
            expected = {"text": case["expected"]["exact"], "terms": case["expected"]["terms"]}
            actual = {mode: ref in all_refs[case["query"], mode] for mode in expected}
            require(actual == expected, "Caso discrepante: " + case["id"])
            cases.append({"id": case["id"], "expected": expected, "observed": actual})
    legacy = evaluate_legacy(index)
    return {"source_commit": index["source_commit"], "projection_sha256": index["projection_sha256"],
            "recipes": len(index["records"]), "query_count": len(reports),
            "oracle_comparisons": len(reports)*2,
            "experiment_comparisons": len(reports)*2 if fixture is not None else 0,
            "passed_cases": len(cases), "cases": cases, "legacy_cases": legacy["passed_cases"],
            "queries": reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()) or output == args.index.resolve():
        parser.error("Salida derivada bajo site/ distinta de entrada")
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    pinned = build_index(serialize(build_projection(ROOT_DIR, fixture["source_commit"])).encode("utf-8"))
    raw = args.index.read_bytes()
    report = {"query_version": QUERY_VERSION, "current_index_sha256": hashlib.sha256(raw).hexdigest(),
              "pinned": evaluate(pinned, fixture), "current": evaluate(json.loads(raw)),
              "scope": "Consistencia de recuperación textual; no precisión culinaria"}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    for name in ("pinned", "current"):
        print(json.dumps({"corpus": name, **{k:v for k,v in report[name].items()
              if k not in ("cases", "queries")}}, ensure_ascii=False, sort_keys=True))
        for item in report[name]["queries"]:
            print(json.dumps({"corpus": name, **item}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
