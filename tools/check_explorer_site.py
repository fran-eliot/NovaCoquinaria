"""Verifica destinos y recursos del explorador en el HTML construido."""
import argparse
import json
from pathlib import Path
from urllib.parse import unquote
import hashlib


def check_site(site):
    root = site.resolve()
    raw = (root / "culinary_explorer.json").read_bytes()
    catalog = json.loads(raw)
    required = ("index.html", "culinary-explorer.html", "assets/culinary-explorer.css",
                "assets/culinary-explorer-ui.mjs", "assets/culinary-explorer-search.mjs")
    for path in required:
        if not (root / path).is_file():
            raise ValueError(f"Recurso ausente: {path}")
    if 'href="culinary-explorer.html"' not in (root / "index.html").read_text(encoding="utf-8"):
        raise ValueError("Acceso desde inicio ausente")
    seen = set()
    for recipe in catalog["recipes"]:
        href = unquote(recipe["href"])
        destination = (root / href).resolve()
        if not destination.is_relative_to(root) or not destination.is_file() or destination in seen:
            raise ValueError(f"Destino inválido: {href}")
        seen.add(destination)
    if len(seen) != catalog["recipe_count"]:
        raise ValueError("Inventario inconsistente")
    return {"source_commit": catalog["source_commit"], "catalog_sha256": hashlib.sha256(raw).hexdigest(),
            "recipes": len(seen), "resources": len(required)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    args = parser.parse_args()
    print(json.dumps(check_site(args.site), ensure_ascii=False))
