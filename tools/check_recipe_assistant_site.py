"""Contraste de todos los datos y destinos publicados del asistente."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_site(site):
    root = site.resolve()
    catalog = json.loads((root / "culinary_explorer.json").read_bytes())
    directory = root / "recipe_assistant"
    manifest = json.loads((directory / "manifest.json").read_bytes())
    require(manifest["schema_version"] == "0.1.0" and
            manifest["index_version"] == catalog["index_version"] and
            all(manifest[k] == catalog[k] for k in
                ("source_commit", "index_sha256", "recipe_count")), "Procedencia incompatible")
    recipes = {r["id"]: r for r in catalog["recipes"]}
    require(len(recipes) == catalog["recipe_count"] and
            set(recipes) == set(manifest["recipes"]), "Inventario incompatible")
    for path in ("recipe-assistant.html", "assets/recipe-assistant.css",
                 "assets/recipe-assistant-ui.mjs", "assets/recipe-assistant-session.mjs"):
        require((root / path).is_file(), f"Recurso ausente: {path}")

    def destination(href):
        path = (root / unquote(href)).resolve()
        require(path.is_relative_to(root) and path.is_file(), f"Destino ausente: {href}")

    expected_files = {"manifest.json"}
    techniques = set()
    for identity, entry in manifest["recipes"].items():
        name = hashlib.sha256(identity.encode()).hexdigest() + ".json"
        require(name == entry["file"] and name not in expected_files, "Nombre incompatible")
        expected_files.add(name)
        raw = (directory / name).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == entry["sha256"], "Huella incorrecta")
        record = json.loads(raw)
        explorer = recipes[identity]
        require(record["id"] == identity and record["schema_version"] == manifest["schema_version"] and
                all(record[k] == manifest[k] for k in ("index_version", "source_commit", "index_sha256")) and
                record["source_sha256"] == entry["source_sha256"] and
                record["href"] == entry["href"] == explorer["href"] and
                all(record[k] == explorer[k] for k in ("title", "source_path", "evidence")),
                f"Registro incompatible: {identity}")
        fields = ("position", "raw", "name", "optionality", "source_location")
        require([{k: e[k] for k in fields} for e in record["ingredients"]] ==
                [{k: e[k] for k in fields} for e in explorer["ingredients"]],
                f"Ingredientes incompatibles: {identity}")
        destination(record["href"])
        for technique in record["techniques"]:
            destination(technique["href"])
            techniques.add(technique["href"])
    require({p.name for p in directory.iterdir()} == expected_files, "Archivos inesperados")
    return {"source_commit": manifest["source_commit"], "index_sha256": manifest["index_sha256"],
            "recipes": len(recipes), "files": len(expected_files), "technique_destinations": len(techniques)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    args = parser.parse_args()
    print(json.dumps(check_site(args.site), ensure_ascii=False))
