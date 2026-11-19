"""Proyección reproducible por receta, con contexto íntegro y origen verificable."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

from audit_inventory import RECIPE_MODULES
from build_recipe_index import digest, nonempty, require, serialize, unique_object, reject_constant
from extract_recipe_metadata import snapshot_bytes
from extract_recipe_content import extract_sections, extract_steps, norm

SCHEMA_VERSION = "0.1.0"


def safe_path(path):
    return (nonempty(path) and path.endswith(".md") and
            not any(c in path for c in "\\:#?") and
            not any(ord(c) < 32 or ord(c) == 127 for c in path) and
            all(p not in ("", ".", "..") for p in path.split("/")))


def href(path):
    return quote(path[:-3] + ".html", safe="/")


def check_location(loc, count):
    require(isinstance(loc, dict) and type(loc.get("start_line")) is int and
            type(loc.get("end_line")) is int and
            1 <= loc["start_line"] <= loc["end_line"] <= count,
            "Localizador fuera de fuente")


def project_recipe(record, identity, commit, index_hash, docs, read_source):
    source = record["source"]
    path = source["path"]
    require(nonempty(identity) and record["id"] == identity and
            source["commit"] == commit and digest(source["sha256"], 64) and
            safe_path(path) and path.split("/")[0] == record["physical_module"] and
            record["physical_module"] in RECIPE_MODULES, "Identidad o ruta inválida")
    target = (docs / path).resolve()
    require(target.is_relative_to(docs) and target.is_file(), "Ficha no publicada")
    raw = read_source(commit, path)
    require(hashlib.sha256(raw).hexdigest() == source["sha256"], "Huella de fuente incorrecta")
    lines = raw.decode("utf-8-sig").splitlines()
    sections = record["sections"]
    require(sections == extract_sections(raw), "Secciones inconsistentes con fuente")
    require(record["steps"] == extract_steps(sections), "Pasos inconsistentes con fuente")
    for section in sections:
        check_location(section["source_location"], len(lines))
    ingredients = []
    for position, entry in enumerate(record["ingredients"]):
        check_location(entry["source_location"], len(lines))
        require(nonempty(entry["raw"]) and isinstance(entry["quantity"], dict) and
                entry["optionality"] in ("required", "optional", "unknown"),
                "Ingrediente inválido")
        ingredients.append({"position": position, **{k: entry[k] for k in
            ("raw", "name", "group", "quantity", "optionality", "source_location")}})
    for order, step in enumerate(record["steps"], 1):
        require(step["order"] == order and nonempty(step["text"]), "Orden inválido")
        check_location(step["source_location"], len(lines))
    declarations = record["durations"] + ([record["yield"]] if record["yield"] else [])
    for declaration in declarations:
        check_location(declaration["source_location"], len(lines))
        require(nonempty(declaration["raw"]), "Declaración inválida")
    evidence = record["evidence"]
    require(evidence["status"] in ("prepared", "pending", "unknown"), "Evidencia inválida")
    for claim in evidence["claims"]:
        check_location(claim["source_location"], len(lines))
    # No se intenta delimitar automáticamente toda advertencia: se conserva
    # el cuerpo completo, incluidos antecedentes, tablas y texto no reconocido.
    start = next(i + 1 for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    require(lines[0].strip() == "---", "Front matter inválido")
    context = {"mode": "full_source", "text": "\n".join(lines[start:]),
               "source_location": {"start_line": start+1, "end_line": len(lines)}}
    mise = []
    active = None
    for section in sections:
        if active is not None and section["level"] <= active:
            active = None
        if norm(section["heading"] or "").strip() == "mise en place":
            active = section["level"]
        if active is not None:
            mise.append(section)
    techniques = []
    for ref in record["references"]:
        path_ref = ref.get("resolved_path")
        if ref["status"] != "resolved" or not safe_path(path_ref) or not path_ref.startswith("00_Bases/03_Tecnicas/"):
            continue
        dest = (docs / path_ref).resolve()
        if not dest.is_relative_to(docs) or not dest.is_file():
            continue
        check_location(ref["source_location"], len(lines))
        techniques.append({"label": ref["label"], "href": href(path_ref),
                           "source_location": ref["source_location"], "source_path": path_ref})
    return {"schema_version": SCHEMA_VERSION, "index_version": "0.2.0",
            "source_commit": commit, "index_sha256": index_hash,
            "id": identity, "title": record["title"], "source_path": path,
            "source_sha256": source["sha256"], "href": href(path),
            "ingredients": ingredients, "steps": record["steps"],
            "yield": record["yield"], "durations": record["durations"],
            "evidence": evidence, "mise_en_place": mise, "context": context,
            "techniques": techniques,
            "diagnostics": [d for d in record["diagnostics"] if d["field"] in
                            ("steps", "yield", "durations", "evidence")]}


def build_assistant(raw, docs, read_source):
    index = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                       parse_constant=reject_constant)
    require(isinstance(index, dict) and (index.get("index_version"), index.get("stage")) ==
            ("0.2.0", "recipe_index_ingredients_preview"), "Índice incompatible")
    commit = index["source_commit"]
    require(digest(commit, 40), "Commit inválido")
    records = index["records"]
    require(isinstance(records, dict) and len(records) == index["inventory"]["recipes"],
            "Inventario inconsistente")
    index_hash = hashlib.sha256(raw).hexdigest()
    docs = docs.resolve()
    files, entries, paths = {}, {}, {}
    for identity, record in sorted(records.items()):
        recipe = project_recipe(record, identity, commit, index_hash, docs, read_source)
        path = recipe["source_path"]
        require(path not in paths, "Ruta duplicada")
        paths[path] = identity
        filename = hashlib.sha256(identity.encode("utf-8")).hexdigest() + ".json"
        require(filename not in files, "Colisión de nombre de archivo")
        data = serialize(recipe).encode("utf-8")
        files[filename] = data
        entries[identity] = {"file": filename, "sha256": hashlib.sha256(data).hexdigest(),
                             "source_sha256": recipe["source_sha256"], "href": recipe["href"]}
    require(paths == index["by_path"], "Inventario de rutas inconsistente")
    manifest = {"schema_version": SCHEMA_VERSION, "index_version": "0.2.0",
                "source_commit": commit, "index_sha256": index_hash,
                "recipe_count": len(entries), "recipes": entries}
    files["manifest.json"] = serialize(manifest).encode("utf-8")
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--docs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    try:
        require(not args.output.exists(), "El directorio de salida debe ser nuevo")
        files = build_assistant(args.index.read_bytes(), args.docs,
                                lambda commit, path: snapshot_bytes(root, commit, path))
        args.output.mkdir(parents=True)
        for name, data in files.items():
            (args.output / name).write_bytes(data)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.exit(1, f"Proyección fallida: {exc}\\n")
    print(f"Recipe Assistant: {len(files)-1} recetas y manifiesto")


if __name__ == "__main__":
    main()
