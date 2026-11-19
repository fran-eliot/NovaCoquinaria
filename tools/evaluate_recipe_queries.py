"""Evaluación dirigida de consultas sobre un índice previamente contrastado."""
import argparse
from collections import Counter
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path

from query_recipe_index import query, QUERY_VERSION
from common import ROOT_DIR


def check(condition, message):
    if not condition:
        raise ValueError(message)


def clause(mode, value, option=None):
    return {"mode": mode, "value": value, "optionality": option}


# Expectativas parciales revisadas contra documentos del corte #234.
# Los casos negativos por ID no implican ausencia en todo el corpus.
CASES = [
    ("Q-01", {"id": "REC-0017"}, [], ["REC-0017"]),
    ("Q-02", {"id": "REC-0017", "path": "05_Carnes/curry_amarillo_de_pollo.md"}, [], ["REC-0017"]),
    ("Q-03", {"id": "REC-0017", "title": " CURRY AMARILLO DE POLLO "}, [], ["REC-0017"]),
    ("Q-04", {"id": "REC-0017", "document_status": "estable", "evidence_status": "pending"}, [], ["REC-0017"]),
    ("Q-05", {"id": "REC-0017", "evidence_status": "prepared"}, [], []),
    ("Q-06", {"id": "REC-0017"}, [clause("explicit", "ING-0012", "required")], ["REC-0017"]),
    ("Q-07", {"id": "REC-0017"}, [clause("candidate", "ING-0012")], []),
    ("Q-08", {"id": "REC-0017"}, [clause("text", "leche de coco"), clause("text", "salsa de soja")], ["REC-0017"]),
    ("Q-09", {"id": "REC-0017"}, [clause("text", "pollo")], []),
    ("Q-10", {"id": "REC-485", "category": "Verduras"}, [clause("candidate", "ING-0022")], ["REC-485"]),
    ("Q-11", {"id": "REC-485"}, [clause("explicit", "ING-0022")], []),
    ("Q-12", {"id": "REC-485"}, [clause("text", "vinagre de vino, opcional según versión", "optional")], ["REC-485"]),
    ("Q-13", {"id": "REC-485"}, [clause("text", "vinagre de vino, opcional según versión", "required")], []),
    ("Q-14", {"id": "REC-0190", "physical_module": "07_Cocina_Asiatica", "evidence_status": "prepared"}, [], ["REC-0190"]),
    ("Q-15", {"id": "REC-0079"}, [clause("text", "lemon curd")], []),
    ("Q-16", {"id": "REC-0017", "physical_module": "08_Postres"}, [], []),
]


def temporal_coverage(records):
    """Cuenta declaraciones utilizables, no tiempos inferidos."""
    time = Counter()
    yields = Counter()
    units = Counter()
    for record in records:
        totals = [d for d in record["durations"] if d["phase"] == "declared_total"]
        if not totals:
            time["no_declared_total"] += 1
        elif len(totals) != 1:
            time["multiple_declared_totals"] += 1
        elif totals[0]["min"] is None or totals[0]["max"] is None:
            time["unparsed_declared_total"] += 1
        elif totals[0]["unit"] in ("min", "h"):
            time["single_numeric_declared_total"] += 1
        else:
            time["unsupported_unit"] += 1
        value = record["yield"]
        if value is None:
            yields["absent_or_ambiguous"] += 1
        elif value["min"] is None or value["max"] is None:
            yields["unparsed"] += 1
        else:
            yields["numeric"] += 1
            units[value["unit"]] += 1
    return {"duration": dict(time), "yield": dict(yields), "yield_units": dict(units)}


def evaluate(index):
    results = []
    for case_id, filters, ingredients, expected in CASES:
        observed = query(index, filters, ingredients)
        ids = [r["id"] for r in observed["results"]]
        check(ids == expected and observed["count"] == len(expected),
              f"{case_id}: esperado {expected}, observado {ids}")
        check(observed == query(index, filters, ingredients), f"{case_id}: no determinista")
        results.append({"case": case_id, "expected": expected, "observed": ids,
                        "query": observed["query"], "results": observed["results"]})
    # Unfiltered query must recover the entire inventory once.
    all_results = query(index)
    check([r["id"] for r in all_results["results"]] == sorted(index["records"]),
          "Inventario de consulta incompleto")
    # Distinguish invalid input from legitimate empty results.
    invalid = [({"evidence_status": "cooked"}, []),
               ({}, [clause("fuzzy", "ajo")]),
               ({"id": "REC-0017"}, [clause("text", " ")])]
    for filters, ingredients in invalid:
        try:
            query(index, filters, ingredients)
        except ValueError:
            continue
        raise ValueError("Consulta inválida aceptada")
    samples = []
    for filters, ingredients in [({"physical_module": "07_Cocina_Asiatica"}, [clause("text", "salsa de soja")]),
                                 ({}, [clause("text", "ajo")]),
                                 ({}, [clause("explicit", "ING-0012")]),
                                 ({}, [clause("candidate", "ING-0012")]),
                                 ({"evidence_status": "prepared"}, [])]:
        result = query(index, filters, ingredients)
        samples.append({"query": result["query"], "count": result["count"],
                        "first_results": result["results"][:3]})
    return {"source_commit": index["source_commit"], "index_version": index["index_version"],
            "query_version": QUERY_VERSION, "passed_cases": len(results),
            "rejected_invalid_queries": len(invalid), "inventory_count": all_results["count"],
            "cases": results, "samples": samples,
            "temporal_coverage": temporal_coverage(index["records"].values()),
            "scope": "Contraste dirigido; no mide precisión ni exhaustividad culinaria"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()) or output == args.index.resolve():
        parser.error("Salida bajo site/, distinta de la entrada")
    try:
        raw = args.index.read_bytes()
        report = evaluate(json.loads(raw))
        report["index_sha256"] = hashlib.sha256(raw).hexdigest()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True,
                                     indent=2) + "\n", encoding="utf-8")
        print(json.dumps({k: v for k, v in report.items() if k not in ("cases", "samples")},
                         ensure_ascii=False, sort_keys=True))
        for sample in report["samples"]:
            print(json.dumps({"query": sample["query"], "count": sample["count"],
                              "ids": [r["id"] for r in sample["first_results"]]},
                             ensure_ascii=False, sort_keys=True))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"Evaluación fallida: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
