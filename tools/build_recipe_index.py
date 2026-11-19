"""Índice básico reconstruible sobre una proyección de recetas serializada."""
from __future__ import annotations

import argparse
from collections import defaultdict
from copy import deepcopy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import unicodedata

from common import ROOT_DIR

INDEX_VERSION = "0.1.0"
SUPPORTED_INPUT = ("0.1.0", "0.4.6", "recipe_projection_preview")


def text_key(value: str) -> str:
    return unicodedata.normalize("NFC", " ".join(value.casefold().split()))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def digest(value, length):
    return isinstance(value, str) and re.fullmatch(
        rf"[0-9a-f]{{{length}}}", value) is not None


def serialize(index):
    return json.dumps(index, ensure_ascii=False, sort_keys=True,
                      indent=2, allow_nan=False) + "\n"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Clave JSON duplicada: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"Constante JSON no válida: {value}")


def build_index(raw: bytes) -> dict:
    """Consume los bytes de entrada y conserva su huella exacta."""
    projection = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object,
                            parse_constant=reject_constant)
    require(isinstance(projection, dict), "Proyección no es un objeto")
    require(tuple(projection.get(k) for k in
                  ("contract_version", "extractor_version", "stage"))
            == SUPPORTED_INPUT, "Versión o etapa de entrada no soportada")
    commit = projection.get("source_commit")
    require(digest(commit, 40), "Commit de origen inválido")
    records = projection.get("recipes")
    inventory = projection.get("inventory")
    require(isinstance(records, list) and isinstance(inventory, dict),
            "Recetas o inventario inválidos")
    count = inventory.get("recipe_documents")
    require(type(count) is int and count == len(records),
            "Recuento de inventario inconsistente")

    by_id, by_path = {}, {}
    facets = {key: defaultdict(list) for key in
              ("physical_module", "category", "document_status", "evidence_status")}
    titles = defaultdict(list)
    for record in records:
        require(isinstance(record, dict), "Registro inválido")
        identity = record.get("id")
        require(nonempty(identity), "ID de receta inválido")
        require(identity not in by_id, f"ID duplicado: {identity}")
        require(record.get("contract_version") == SUPPORTED_INPUT[0],
                f"{identity}: contrato incompatible")
        source = record.get("source")
        require(isinstance(source, dict), f"{identity}: fuente inválida")
        path = source.get("path")
        require(nonempty(path) and not path.startswith("/") and
                "\\" not in path and all(part not in ("", ".", "..")
                for part in path.split("/")) and PurePosixPath(path).suffix == ".md",
                f"{identity}: ruta inválida")
        require(path not in by_path, f"Ruta duplicada: {path}")
        require(source.get("commit") == commit and digest(source.get("sha256"), 64),
                f"{identity}: procedencia inconsistente")
        metadata, evidence = record.get("metadata"), record.get("evidence")
        require(isinstance(metadata, dict) and metadata.get("id") == identity
                and metadata.get("tipo") == "receta", f"{identity}: metadatos inválidos")
        title = record.get("title")
        require(nonempty(title) and metadata.get("titulo") == title,
                f"{identity}: título inválido")
        require(isinstance(evidence, dict) and evidence.get("status") in
                ("prepared", "pending", "unknown"), f"{identity}: evidencia inválida")
        require(all(k in record for k in ("physical_module", "category")),
                f"{identity}: faltan metadatos de clasificación")
        for key, value in (
            ("physical_module", record["physical_module"]),
            ("category", record["category"]),
            ("document_status", metadata.get("estado")),
            ("evidence_status", evidence["status"]),
        ):
            require(value is None or isinstance(value, str),
                    f"{identity}: metadato no textual: {key}")
            if value is not None:
                facets[key][value].append(identity)
        for field in ("ingredients", "steps", "sections", "references",
                      "durations", "diagnostics"):
            require(isinstance(record.get(field), list), f"{identity}: {field} inválido")
        require("yield" in record and (record["yield"] is None or
                isinstance(record["yield"], dict)), f"{identity}: rendimiento inválido")
        by_id[identity] = deepcopy(record)
        by_path[path] = identity
        titles[text_key(title)].append(identity)

    return {
        "index_version": INDEX_VERSION,
        "contract_version": SUPPORTED_INPUT[0],
        "extractor_version": SUPPORTED_INPUT[1],
        "source_commit": commit,
        "stage": "recipe_index_core_preview",
        "projection_sha256": hashlib.sha256(raw).hexdigest(),
        "records": by_id,
        "by_path": by_path,
        "facets": {field: {value: sorted(ids) for value, ids in groups.items()}
                   for field, groups in facets.items()},
        "by_title": {value: sorted(ids) for value, ids in titles.items()},
        "inventory": {"recipes": len(by_id), "paths": len(by_path),
                      "title_keys": len(titles),
                      "facet_keys": {field: len(groups) for field, groups in facets.items()}},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = (ROOT_DIR / args.input).resolve()
    output = (ROOT_DIR / args.output).resolve()
    if not output.is_relative_to((ROOT_DIR / "site").resolve()) or source == output:
        parser.error("--output debe estar dentro de site/ y ser distinto de --input")
    try:
        index = build_index(source.read_bytes())
        data = serialize(index).encode("utf-8")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
    except (ValueError, TypeError, OSError) as exc:
        parser.exit(1, f"Indexación fallida: {exc}\n")
    print(json.dumps(index["inventory"], ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
