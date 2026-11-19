"""Métricas descriptivas de la proyección; no estiman exactitud culinaria."""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

from common import ROOT_DIR


def metric(n, d):
    return {"count": n, "denominator": d, "percent": round(100*n/d, 2) if d else None}


def distribution(items, key):
    return dict(sorted(Counter(item.get(key, "unknown") or "unknown" for item in items).items()))


def summarize(records):
    n=len(records)
    ingredients=[i for r in records for i in r["ingredients"]]
    quantities=[i["quantity"] for i in ingredients]
    durations=[d for r in records for d in r["durations"]]
    references=[ref for r in records for ref in r["references"]]
    internal=[ref for ref in references if ref["status"] not in ("external","local_anchor")]
    diagnostics=[d for r in records for d in r["diagnostics"]]
    fields={
        "ingredients": lambda r: bool(r["ingredients"]),
        "steps": lambda r: bool(r["steps"]),
        "sections": lambda r: bool(r["sections"]),
        "category": lambda r: r["category"] is not None,
        "yield_declared": lambda r: r["yield"] is not None,
        "yield_numeric": lambda r: r["yield"] is not None and r["yield"]["min"] is not None,
        "duration_declared": lambda r: bool(r["durations"]),
        "duration_numeric": lambda r: any(d["min"] is not None for d in r["durations"]),
        "references": lambda r: bool(r["references"]),
        "evidence_recognized": lambda r: r["evidence"]["status"] in ("prepared","pending"),
    }
    return {
        "recipes":n,
        "field_presence":{k:metric(sum(test(r) for r in records),n) for k,test in fields.items()},
        "ingredient_lines":len(ingredients),
        "quantity_status":distribution(quantities,"status"),
        "quantity_numeric":metric(sum(q["status"] in ("exact","range") for q in quantities),len(quantities)),
        "ingredient_resolution":distribution(ingredients,"resolution"),
        "ingredient_explicit":metric(sum(i["resolution"]=="explicit" for i in ingredients),len(ingredients)),
        "optionality":distribution(ingredients,"optionality"),
        "duration_lines":len(durations),
        "duration_numeric":metric(sum(d["min"] is not None for d in durations),len(durations)),
        "reference_occurrences":len(references),
        "reference_status":distribution(references,"status"),
        "internal_resolved":metric(sum(r["status"]=="resolved" for r in internal),len(internal)),
        "internal_with_id":metric(sum(r["status"]=="resolved" and r["target_id"] is not None for r in internal),len(internal)),
        "evidence_status":distribution([r["evidence"] for r in records],"status"),
        "diagnostic_occurrences":distribution(diagnostics,"code"),
        "recipes_with_diagnostics":metric(sum(bool(r["diagnostics"]) for r in records),n),
    }


def structural_gaps(records):
    """Localizadores y encabezados para revisión, sin inferir causas."""
    gaps = []
    for record in sorted(records, key=lambda item: item["id"]):
        missing = [field for field in ("ingredients", "steps") if not record[field]]
        if not missing:
            continue
        sections = []
        for section in record["sections"]:
            heading = section.get("heading")
            if heading is not None:
                sections.append({
                    "heading": heading,
                    "source_location": section.get("source_location"),
                })
        gaps.append({
            "id": record["id"],
            "path": record["source"]["path"],
            "missing": missing,
            "headings": sections,
        })
    return gaps


def coverage(projection):
    records=projection["recipes"]
    if projection["stage"]!="recipe_projection_preview":
        raise ValueError("Se requiere la proyección completa en etapa preview")
    if len(records)!=projection["inventory"]["recipe_documents"]:
        raise ValueError("Inventario no coincide con registros")
    ids=[r["id"] for r in records]
    if len(set(ids))!=len(ids):
        raise ValueError("IDs duplicados en proyección")
    groups=defaultdict(list)
    affected=defaultdict(list)
    for record in records:
        groups[record["physical_module"] or "(root)"].append(record)
        for code in sorted({d["code"] for d in record["diagnostics"]}):
            affected[code].append({"id":record["id"],"path":record["source"]["path"]})
    return {
        "source_commit":projection["source_commit"],
        "contract_version":projection["contract_version"],
        "extractor_version":projection["extractor_version"],
        "scope":"Presencia y reconocimiento de registros extraídos; no recall, precisión ni validación culinaria.",
        "global":summarize(records),
        "structural_gaps":structural_gaps(records),
        "by_module":{k:summarize(v) for k,v in sorted(groups.items())},
        "affected_recipes":{k:sorted(v,key=lambda item:item["id"]) for k,v in sorted(affected.items())},
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    output=(ROOT_DIR/args.output).resolve()
    if not output.is_relative_to((ROOT_DIR/"site").resolve()):
        parser.error("--output debe estar dentro de site/")
    try:
        projection=json.loads((ROOT_DIR/args.input).read_text(encoding="utf-8"))
        report=coverage(projection)
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_bytes((json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode("utf-8"))
        print(json.dumps({"source_commit":report["source_commit"],"global":report["global"],"structural_gaps":report["structural_gaps"]},ensure_ascii=False,indent=2))
    except (ValueError,KeyError,TypeError,OSError) as exc:
        parser.exit(1,f"Informe fallido: {exc}\n")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
