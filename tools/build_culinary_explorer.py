"""Proyección pública y reproducible del índice de recetas para Culinary Explorer."""
import argparse
import hashlib
import json
from pathlib import Path
import unicodedata
from urllib.parse import quote

from audit_inventory import RECIPE_MODULES
from build_recipe_index import digest, nonempty, require, serialize, unique_object, reject_constant, text_key
from recipe_retrieval_terms import tokens

SCHEMA_VERSION = "0.1.1"


def unicode_profile():
    """Tablas de Python para no depender de lowercase o categorías de JS."""
    fold, spaces, ranges = {}, [], []
    for cp in range(0x110000):
        char = chr(cp)
        if char.casefold() != char:
            fold[str(cp)] = char.casefold()
        if char.isspace():
            spaces.append(cp)
        if char.isalnum():
            if ranges and ranges[-1][1] == cp - 1:
                ranges[-1][1] = cp
            else:
                ranges.append([cp, cp])
    return {"unicode_version": unicodedata.unidata_version, "casefold": fold,
            "spaces": spaces, "alnum_ranges": ranges}



def build_explorer(raw: bytes, docs: Path) -> dict:
    index = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                       parse_constant=reject_constant)
    require(isinstance(index, dict) and
            (index.get("index_version"), index.get("stage")) ==
            ("0.2.0", "recipe_index_ingredients_preview"), "Índice incompatible")
    commit = index.get("source_commit")
    require(digest(commit, 40), "Commit inválido")
    records = index["records"]
    require(isinstance(records, dict) and index["inventory"]["recipes"] == len(records),
            "Inventario inconsistente")
    recipes, paths, expected_text = [], {}, {}
    root = docs.resolve()
    for identity, record in sorted(records.items()):
        source = record["source"]
        path = source["path"]
        module = record["physical_module"]
        require(nonempty(identity) and record["id"] == identity and
                source["commit"] == commit and digest(source["sha256"], 64),
                "Identidad o procedencia inválida")
        require(isinstance(path, str) and module in RECIPE_MODULES and
                path.split("/")[0] == module and path.endswith(".md") and
                all(part not in ("", ".", "..") for part in path.split("/")) and
                not any(c in path for c in "\\:#?") and path not in paths and
                Path(path).name != "README.md", "Ruta de receta inválida")
        file = (root / path).resolve()
        require(file.is_relative_to(root) and file.is_file(), f"Fuente no publicada: {path}")
        paths[path] = identity
        title = record["title"]
        evidence = record["evidence"]
        require(nonempty(title) and isinstance(evidence, dict) and
                evidence.get("status") in ("prepared", "pending", "unknown"),
                "Título o evidencia inválidos")
        require(isinstance(record["ingredients"], list), "Ingredientes inválidos")
        occurrences = []
        for position, entry in enumerate(record["ingredients"]):
            name, original = entry["name"], entry["raw"]
            option, loc = entry["optionality"], entry["source_location"]
            require((name is None or isinstance(name, str)) and nonempty(original)
                    and option in ("required", "optional", "unknown")
                    and type(loc["start_line"]) is int and type(loc["end_line"]) is int
                    and 0 < loc["start_line"] <= loc["end_line"], "Ocurrencia inválida")
            key = text_key(name) if name is not None else ""
            if key:
                expected_text.setdefault(key, []).append({"recipe_id": identity, "position": position})
            occurrences.append({"position": position, "name": name, "raw": original,
                                "optionality": option, "source_location": loc,
                                "tokens": list(tokens(key))})
        recipes.append({"id": identity, "title": title, "title_tokens": list(tokens(title)),
                        "title_key": text_key(title), "physical_module": module,
                        "evidence": evidence, "source_path": path,
                        "href": quote(path[:-3] + ".html", safe="/"),
                        "ingredients": occurrences})
    require(paths == index["by_path"], "Índice de rutas inconsistente")
    require(expected_text == index["ingredients"]["by_text"], "Postings textuales inconsistentes")
    return {"schema_version": SCHEMA_VERSION, "index_version": "0.2.0",
            "source_commit": commit, "index_sha256": hashlib.sha256(raw).hexdigest(),
            "recipe_count": len(recipes), "recipes": recipes,
            "unicode_profile": unicode_profile()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--docs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        require(args.output.resolve() != args.index.resolve(), "Salida igual a entrada")
        result = build_explorer(args.index.read_bytes(), args.docs)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(serialize(result).encode("utf-8"))
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.exit(1, f"Proyección fallida: {exc}\n")
    print(f"Culinary Explorer: {result['recipe_count']} recetas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
