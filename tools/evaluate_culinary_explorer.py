"""Contraste del adaptador JavaScript con el motor Python y un recorrido de títulos."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import unicodedata

from query_recipe_index import query
from recipe_retrieval_terms import tokens
from build_recipe_index import text_key

ROOT = Path(__file__).resolve().parent.parent


def title_matches(title, value, mode):
    if mode == "exact":
        return text_key(title) == text_key(value)
    def words(s):
        return re.findall(r"[^\W_]+", unicodedata.normalize("NFC", s.casefold()))
    hay, needle = words(title), words(value)
    return bool(needle) and any(hay[i:i+len(needle)] == needle for i in range(len(hay)))


def expected(index, request):
    if "lexical" in request:
        value = request["lexical"]
        return {"key": text_key(value), "tokens": list(tokens(value))}
    filters = {}
    for field, target in (("module", "physical_module"), ("evidence", "evidence_status")):
        if field in request:
            filters[target] = request[field]
    clauses = [{"mode": "terms", "value": v} for v in request.get("ingredients", [])]
    title = request.get("title")
    mode = request.get("titleMode", "terms")
    if title is not None and not (text_key(title) if mode == "exact" else tokens(title)):
        return {"error": True}
    try:
        rows = query(index, filters, clauses)["results"]
    except ValueError:
        return {"error": True}
    result = []
    for row in rows:
        if title is not None and not title_matches(row["title"], title, mode):
            continue
        matches = []
        for reason in row["matches"]:
            if reason["field"] == "ingredient":
                matches.append([{k: e[k] for k in ("position", "name", "raw",
                    "optionality", "source_location")} for e in reason["occurrences"]])
        result.append({"id": row["id"], "matches": matches})
    return {"rows": result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = args.index.read_bytes()
    index = json.loads(raw)
    catalog = json.loads(args.catalog.read_bytes())
    if catalog["index_sha256"] != hashlib.sha256(raw).hexdigest() or catalog["source_commit"] != index["source_commit"]:
        raise ValueError("Catálogo e índice no corresponden")
    requests = [{}, *[{"ingredients": [v]} for v in (
        "ajo", "ajo negro", "salsa de soja", "leche de coco", "sal", "sin sal",
        "leche o nata", "pimiento", "aji", "ají", "soja", "aj", "noexistexyz",
        "SALSA_DE_SOJA", "---")],
        {"ingredients": ["ajo", "salsa de soja"]},
        {"ingredients": ["ajo", "salsa de soja"], "module": "07_Cocina_Asiatica"},
        {"ingredients": ["ajo"], "evidence": "prepared"},
        {"evidence": "pending"}, {"evidence": "unknown"},
        {"title": "arroz"}, {"title": "ajo"}, {"title": "---"},
        {"title": "noexistexyz"}, {"title": "arroz", "ingredients": ["ajo"]}]
    for module in sorted(index["facets"]["physical_module"]):
        requests.append({"module": module})
    for record in list(index["records"].values())[::max(1, len(index["records"])//12)]:
        requests.append({"title": record["title"], "titleMode": "exact"})
    requests.extend({"lexical": v} for v in (
        "Straße", "ΟΣ ς", "AJO__NEGRO", "  ajo\u001cnegro ", "aji\u0301",
        "İ", "½ ²", "中文", "a\u200bb", "ﬃ", "Σ", "🧄", "\u00a0ajo\tnegro "))
    actual = json.loads(subprocess.check_output(
        ["node", str(ROOT / "tools/explorer_search_driver.mjs"), str(args.catalog)],
        input=json.dumps(requests), text=True, encoding="utf-8"))
    if len(actual) != len(requests):
        raise ValueError("Número de respuestas incorrecto")
    reports = []
    for request, answer in zip(requests, actual):
        reference = expected(index, request)
        if answer != reference:
            raise ValueError(f"Discrepancia: {request!r}")
        reports.append({"request": request, "passed": True,
                        "count": len(answer["rows"]) if "rows" in answer else None})
    report = {"source_commit": index["source_commit"], "index_sha256": catalog["index_sha256"],
              "catalog_sha256": hashlib.sha256(args.catalog.read_bytes()).hexdigest(),
              "unicode_version": catalog["unicode_profile"]["unicode_version"],
              "passed": len(reports), "cases": reports}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Culinary Explorer Search: {len(reports)} contrastes superados")


if __name__ == "__main__":
    main()
