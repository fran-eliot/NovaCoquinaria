"""Inventario de rutas versionadas, independiente de la madurez semántica."""
from collections import Counter
from pathlib import Path, PurePosixPath
import argparse
import json
import subprocess

from common import ROOT_DIR

RECIPE_MODULES = (
    "01_Arroces", "02_Pastas", "03_Legumbres", "04_Verduras",
    "05_Carnes", "06_Pescados_y_Mariscos", "07_Cocina_Asiatica",
    "08_Postres", "09_Bebidas", "10_Horno",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT_DIR, encoding="utf-8"
    )


def build_inventory(files: list[str], commit: str) -> dict:
    markdown = [PurePosixPath(p) for p in files if p.endswith(".md")]
    modules = Counter(
        p.parts[0] for p in markdown
        if p.parts[0] in RECIPE_MODULES and p.name != "README.md"
    )
    return {
        "commit": commit,
        "scope": "Git tracked Markdown paths; recipe modules exclude README.md",
        "markdown_files": len(markdown),
        "recipe_paths": sum(modules.values()),
        "recipe_paths_by_module": {name: modules[name] for name in RECIPE_MODULES},
        "ingredient_paths": sum(
            p.parts[0] == "11_Despensa" and p.name not in {"README.md", "BACKLOG.md"}
            for p in markdown
        ),
        "technique_paths": sum(
            p.parts[:2] == ("00_Bases", "03_Tecnicas") and p.name != "README.md"
            for p in markdown
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    commit = git("rev-parse", "HEAD").strip()
    files = git("ls-tree", "-r", "--name-only", "-z", commit).split("\0")
    inventory = build_inventory([p for p in files if p], commit)
    output = ROOT_DIR / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(inventory, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
