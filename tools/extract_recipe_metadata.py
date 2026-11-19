"""Primera proyección parcial de recetas desde un snapshot Git inmutable."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

import yaml

from audit_inventory import RECIPE_MODULES
from common import ROOT_DIR, requires_frontmatter
from extract_recipe_ingredients import extract_ingredients
from extract_recipe_content import extract_content
from extract_recipe_details import general_fields, extract_references
from ingredient_identity_candidates import build_catalog, annotate

CONTRACT_VERSION = "0.1.0"
EXTRACTOR_VERSION = "0.4.5"
FRONT_MATTER = re.compile(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)",
                          re.MULTILINE | re.DOTALL)


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=root)


def snapshot_commit(root: Path, ref: str) -> str:
    return git(root, "rev-parse", "--verify", "--end-of-options",
               f"{ref}^{{commit}}").decode("ascii").strip()


def snapshot_paths(root: Path, commit: str) -> list[str]:
    raw = git(root, "ls-tree", "-r", "-z", "--name-only", commit)
    return sorted(p.decode("utf-8") for p in raw.split(b"\0")
                  if p.endswith(b".md") and
                  PurePosixPath(p.decode("utf-8")).name.lower() != "readme.md")


def snapshot_bytes(root: Path, commit: str, path: str) -> bytes:
    return git(root, "show", f"{commit}:{path}")


def json_default(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(f"Metadato no serializable: {type(value).__name__}")


def read_metadata(raw: bytes, path: str) -> tuple[dict | None, str | None]:
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path}: Markdown no UTF-8") from exc
    match = FRONT_MATTER.match(text)
    if not match:
        if text.startswith("---\n") or text.startswith("---\r\n"):
            raise ValueError(f"{path}: Front Matter sin cierre")
        return None, None
    original = match.group(1)
    try:
        metadata = yaml.safe_load(original)
        node = yaml.compose(original, Loader=yaml.SafeLoader)
    except yaml.YAMLError as exc:
        raise ValueError(f"{path}: Front Matter YAML inválido") from exc
    if not isinstance(metadata, dict) or not isinstance(node, yaml.MappingNode):
        raise ValueError(f"{path}: Front Matter no es un mapa")
    if len(node.value) != len(metadata):
        raise ValueError(f"{path}: claves YAML duplicadas o combinación no admitida")
    if metadata.get("tipo") == "receta":
        # YAML interpreta versiones antiguas como 1.0 como números.
        # El valor léxico de un escalar es la versión documental.
        for key, value in node.value:
            if key.value == "version" and isinstance(value, yaml.ScalarNode):
                metadata["version"] = value.value
    return metadata, original


def project_metadata(raw: bytes, path: str, commit: str) -> dict | None:
    metadata, original = read_metadata(raw, path)
    if metadata is None or metadata.get("tipo") != "receta":
        return None
    for field in ("id", "titulo", "version"):
        if not isinstance(metadata.get(field), str) or not metadata[field].strip():
            raise ValueError(f"{path}: {field} ausente o no textual")
    parts = PurePosixPath(path).parts
    return {
        "contract_version": CONTRACT_VERSION,
        "id": metadata["id"],
        "source": {
            "commit": commit,
            "path": path,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "frontmatter_raw": original,
            "frontmatter_location": {
                "start_line": 1,
                "end_line": original.count("\n") + 3,
            },
        },
        "metadata": metadata,
        "title": metadata["titulo"],
        "physical_module": parts[0] if len(parts) > 1 else None,
        "category": metadata.get("categoria"),
        "diagnostics": [],
    }


def build_projection(root: Path, ref: str = "HEAD") -> dict:
    commit = snapshot_commit(root, ref)
    records = []
    ids = set()
    numeric_ids = {}
    recipe_paths = 0
    paths_without_recipe = []
    recipes_outside_modules = []
    paths = snapshot_paths(root, commit)
    ingredient_lookup = {}
    ingredient_documents = {}
    document_lookup = {}
    known_paths = {p.decode('utf-8') for p in git(root, 'ls-tree', '-r', '-z', '--name-only', commit).split(b'\0') if p}
    recipe_sources = {}
    for path in paths:
        parts = PurePosixPath(path).parts
        module_path = parts[0] in RECIPE_MODULES
        if module_path:
            recipe_paths += 1
        raw = snapshot_bytes(root, commit, path)
        record = project_metadata(raw, path, commit)
        if record is None:
            fields, _ = read_metadata(raw, path)
            if fields and isinstance(fields.get('id'), str):
                document_lookup[path] = fields['id']
            if fields and fields.get('tipo') == 'ingrediente' and isinstance(fields.get('id'), str):
                ingredient_lookup[path] = fields['id']
                ingredient_documents[path] = fields
            if module_path:
                paths_without_recipe.append(path)
                # Una fuente culinaria sin Front Matter no puede clasificarse.
                if read_metadata(raw, path)[0] is None and requires_frontmatter(path):
                    raise ValueError(f"{path}: Front Matter ausente")
            continue
        identity = record["id"]
        document_lookup[path] = identity
        if identity in ids:
            raise ValueError(f"{path}: ID de receta duplicado: {identity}")
        ids.add(identity)
        match = re.fullmatch(r"REC-(\d+)", identity)
        if match:
            numeric_ids.setdefault(int(match.group(1)), []).append(record)
        if not module_path:
            recipes_outside_modules.append(path)
        records.append(record)
        recipe_sources[path] = raw
    for group in numeric_ids.values():
        if len(group) > 1:
            for record in group:
                record["diagnostics"].append({
                    "code": "ID_FORMAT_COLLISION",
                    "severity": "warning",
                    "field": "id",
                    "source_location": record["source"]["frontmatter_location"],
                    "description": "Posible equivalencia de formato; IDs conservados: "
                                   + ", ".join(sorted(r["id"] for r in group)),
                })
    catalog = build_catalog(ingredient_documents)
    for record in records:
        path = record['source']['path']
        entries, diagnostics = extract_ingredients(recipe_sources[path], path, ingredient_lookup)
        annotate(entries, catalog)
        record['ingredients'] = entries
        record['diagnostics'].extend(diagnostics)
        content, content_diagnostics = extract_content(recipe_sources[path])
        record.update(content)
        record['diagnostics'].extend(content_diagnostics)
        details, detail_diagnostics = general_fields(record['sections'], record['source']['frontmatter_raw'])
        record.update(details)
        refs, reference_diagnostics = extract_references(record['sections'], path, document_lookup, known_paths)
        record['references'] = refs
        record['diagnostics'].extend(detail_diagnostics + reference_diagnostics)
    return {
        "contract_version": CONTRACT_VERSION,
        "extractor_version": EXTRACTOR_VERSION,
        "stage": "recipe_projection_preview",
        "ingredient_summary": dict(sorted(Counter(e["quantity"]["status"] for r in records for e in r["ingredients"]).items())),
        "source_commit": commit,
        "inventory": {
            "recipe_paths": recipe_paths,
            "recipe_documents": len(records),
            "paths_without_recipe_type": paths_without_recipe,
            "recipes_outside_modules": recipes_outside_modules,
            "by_physical_module": dict(sorted(Counter(
                r["physical_module"] or "(root)" for r in records).items())),
        },
        "recipes": sorted(records, key=lambda record: record["id"]),
    }


def serialize(projection: dict) -> str:
    return json.dumps(projection, ensure_ascii=False, indent=2,
                      sort_keys=True, default=json_default, allow_nan=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="HEAD")
    parser.add_argument("--output", type=Path, required=True,
                        help="Ruta derivada dentro de site/")
    args = parser.parse_args()
    output = (ROOT_DIR / args.output).resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()):
        parser.error("--output debe estar dentro de site/")
    try:
        projection = build_projection(ROOT_DIR, args.ref)
        serialized = serialize(projection)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(serialized.encode("utf-8"))
    except (ValueError, TypeError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Extracción fallida: {exc}\n")
    print(json.dumps(projection["inventory"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
