"""Consultas de solo lectura sobre el índice derivado de recetas 0.2.0."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import unicodedata


QUERY_VERSION = "0.1.0"
MODES = {"text": "by_text", "explicit": "by_explicit_id",
         "candidate": "by_candidate_id"}
FACETS = ("physical_module", "category", "document_status", "evidence_status")


def normalize(value):
    return unicodedata.normalize("NFC", " ".join(value.casefold().split()))


def check(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def query(index, filters=None, ingredients=None):
    """Intersección de todos los filtros; devuelve recetas únicas y motivos."""
    check(isinstance(index, dict) and
          (index.get("index_version"), index.get("stage")) ==
          ("0.2.0", "recipe_index_ingredients_preview"), "Índice incompatible")
    filters = {} if filters is None else filters
    ingredients = [] if ingredients is None else ingredients
    check(isinstance(filters, dict) and isinstance(ingredients, list),
          "Consulta inválida")
    check(set(filters) <= set(FACETS) | {"id", "path", "title"},
          "Filtro desconocido")
    records = index["records"]
    remaining = set(records)
    reasons = {}
    canonical_filters = {}
    for field, value in sorted(filters.items()):
        check(nonempty(value), f"Filtro vacío: {field}")
        if field == "evidence_status":
            check(value in ("prepared", "pending", "unknown"), "Evidencia inválida")
        if field == "id":
            hits = [value] if value in records else []
        elif field == "path":
            found = index["by_path"].get(value)
            hits = [found] if found is not None else []
        elif field == "title":
            hits = index["by_title"].get(normalize(value), [])
        else:
            hits = index["facets"][field].get(value, [])
        canonical_filters[field] = value
        remaining.intersection_update(hits)
        for identity in remaining:
            reasons.setdefault(identity, []).append({"field": field, "value": value})
    canonical_ingredients = []
    for clause in ingredients:
        check(isinstance(clause, dict) and set(clause) <=
              {"mode", "value", "optionality"}, "Condición de ingrediente inválida")
        mode, value = clause.get("mode"), clause.get("value")
        option = clause.get("optionality")
        check(isinstance(mode, str) and mode in MODES and nonempty(value),
              "Modo o valor de ingrediente inválido")
        check(option in (None, "required", "optional", "unknown"),
              "Opcionalidad inválida")
        canonical_ingredients.append({"mode": mode, "value": value, "optionality": option})
        key = normalize(value) if mode == "text" else value
        hits = {}
        for posting in index["ingredients"][MODES[mode]].get(key, []):
            identity, position = posting["recipe_id"], posting["position"]
            entry = records[identity]["ingredients"][position]
            if option is not None and entry["optionality"] != option:
                continue
            matches = {"position": position, "raw": entry["raw"],
                       "name": entry["name"], "optionality": entry["optionality"],
                       "resolution": entry["resolution"],
                       "ingredient_id": entry["ingredient_id"],
                       "source_location": entry["source_location"]}
            if mode == "candidate":
                matches["methods"] = posting["methods"]
                matches["candidate_evidence"] = [m for m in entry["identity_candidates"]
                                                 if m["ingredient_id"] == value]
            hits.setdefault(identity, []).append(matches)
        remaining.intersection_update(hits)
        for identity in remaining:
            reasons.setdefault(identity, []).append({
                "field": "ingredient", "mode": mode, "value": value,
                "optionality": option, "occurrences": hits[identity]})
    results = []
    for identity in sorted(remaining):
        record = records[identity]
        results.append({"id": identity, "title": record["title"],
                        "source": {k: record["source"][k] for k in ("commit", "path", "sha256")},
                        "physical_module": record["physical_module"],
                        "category": record["category"],
                        "document_status": record["metadata"].get("estado"),
                        "evidence": record["evidence"],
                        "matches": reasons.get(identity, [])})
    return {"query_version": QUERY_VERSION, "index_version": index["index_version"],
            "source_commit": index["source_commit"],
            "projection_sha256": index["projection_sha256"],
            "query": {"filters": canonical_filters, "ingredients": canonical_ingredients},
            "count": len(results), "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    for field in ("id", "path", "title", *FACETS):
        parser.add_argument("--" + field.replace("_", "-"))
    parser.add_argument("--ingredient", action="append", nargs=2, default=[],
                        metavar=("MODE", "VALUE"))
    parser.add_argument("--ingredient-with-optionality", action="append", nargs=3,
                        default=[], metavar=("MODE", "VALUE", "OPTIONALITY"))
    args = parser.parse_args()
    filters = {field: getattr(args, field) for field in ("id", "path", "title", *FACETS)
               if getattr(args, field) is not None}
    ingredients = [{"mode": mode, "value": value} for mode, value in args.ingredient]
    ingredients.extend({"mode": mode, "value": value, "optionality": option}
                       for mode, value, option in args.ingredient_with_optionality)
    try:
        index = json.loads(args.index.read_text(encoding="utf-8"))
        result = query(index, filters, ingredients)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False))
    except (ValueError, KeyError, TypeError, IndexError, OSError) as exc:
        parser.exit(1, f"Consulta fallida: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
