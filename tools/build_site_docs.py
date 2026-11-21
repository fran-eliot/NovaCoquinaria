from pathlib import Path
import shutil
import argparse
import hashlib

ROOT = Path(__file__).resolve().parent.parent
SITE_DOCS = ROOT / "site_docs"
HOME_TEMPLATE = ROOT / "tools/templates/home.md"

INCLUDE = [
    "README.md",
    "MANIFESTO.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE.md",
    "GUIA_DE_ESTILO.md",
    "ESPECIFICACION_DE_DOCUMENTOS.md",
    "assets",
    "00_Bases",
    "01_Arroces",
    "02_Pastas",
    "03_Legumbres",
    "04_Verduras",
    "05_Carnes",
    "06_Pescados_y_Mariscos",
    "07_Cocina_Asiatica",
    "08_Postres",
    "09_Bebidas",
    "10_Horno",
    "11_Despensa",
    "12_Plantillas",
    "98_Tablas",
    "docs",
]

IGNORE_DIRS = {
    ".git",
    ".venv",
    "site",
    "site_docs",
    "__pycache__",
}

TEXT_EXTENSIONS = {".md", ".yml", ".yaml"}


def copy_item(relative_path: str) -> None:
    src = ROOT / relative_path
    dst = SITE_DOCS / relative_path

    if not src.exists():
        print(f"SKIP: {relative_path}")
        return

    if src.is_dir():
        shutil.copytree(
            src,
            dst,
            ignore=shutil.ignore_patterns(*IGNORE_DIRS),
        )
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def normalize_links_in_file(path: Path) -> None:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return

    content = path.read_text(encoding="utf-8")

    replacements = {
        "README.md": "index.md",
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    path.write_text(content, encoding="utf-8")


def normalize_links() -> None:
    for path in SITE_DOCS.rglob("*"):
        if path.is_file():
            normalize_links_in_file(path)


def create_index_files() -> None:
    for readme in SITE_DOCS.rglob("README.md"):
        index = readme.parent / "index.md"

        if not index.exists():
            shutil.copy2(readme, index)

        readme.unlink()
        

def create_home_page() -> None:
    content = HOME_TEMPLATE.read_text(encoding="utf-8")
    (SITE_DOCS / "index.md").write_text(content, encoding="utf-8")


def version_application_assets() -> None:
    """Versionar el grafo de recursos estáticos sin modificar las fuentes."""
    assets = SITE_DOCS / "assets"
    names = ("culinary-explorer-ui.mjs", "culinary-explorer-search.mjs",
             "culinary-explorer.css", "recipe-assistant-ui.mjs",
             "recipe-assistant-session.mjs", "recipe-assistant-markdown.mjs",
             "recipe-assistant.css", "culinary-pantry.css", "culinary-pantry-ui.mjs",
             "culinary-pantry-model.mjs", "culinary-pantry-persistence.mjs", "culinary-pantry-transfer.mjs",
             "culinary-shopping.css", "culinary-shopping-ui.mjs", "culinary-shopping-model.mjs",
             "culinary-shopping-persistence.mjs", "culinary-shopping-recipe-transfer.mjs", "culinary-shopping-pantry-coordinator.mjs",
             "culinary-planner.css", "culinary-planner-ui.mjs",
             "culinary-planner-model.mjs", "culinary-planner-persistence.mjs",
             "culinary-planner-recipe-transfer.mjs")
    originals = {name: (assets / name).read_bytes() for name in names}
    digest = hashlib.sha256()
    for name, raw in sorted(originals.items()):
        digest.update(name.encode("utf-8") + b"\0" + raw + b"\0")
    version = digest.hexdigest()[:20]
    # Mantener las rutas antiguas para las páginas que aún estén en caché.
    for name, raw in originals.items():
        path = Path(name)
        destination = assets / f"{path.stem}.{version}{path.suffix}"
        content = raw.decode("utf-8")
        for imported in names:
            target = Path(imported)
            hashed = f"{target.stem}.{version}{target.suffix}"
            content = content.replace(f'"./{imported}"', f'"./{hashed}"')
        destination.write_bytes(content.encode("utf-8"))
    for page in ("culinary-explorer.html", "recipe-assistant.html", "culinary-pantry.html", "culinary-shopping.html", "culinary-planner.html"):
        path = SITE_DOCS / page
        content = path.read_text(encoding="utf-8")
        for name in names:
            target = Path(name)
            hashed = f"{target.stem}.{version}{target.suffix}"
            content = content.replace(f'"assets/{name}"', f'"assets/{hashed}"')
        path.write_bytes(content.encode("utf-8"))


def build_explorer_page() -> None:
    from extract_recipe_metadata import build_projection, snapshot_bytes, serialize as serialize_projection
    from build_recipe_index import build_index, serialize
    from build_culinary_explorer import build_explorer
    from build_recipe_assistant import build_assistant

    projection = serialize_projection(build_projection(ROOT)).encode("utf-8")
    index = serialize(build_index(projection)).encode("utf-8")
    catalog = build_explorer(index, SITE_DOCS)
    (SITE_DOCS / "culinary_explorer.json").write_bytes(serialize(catalog).encode("utf-8"))
    shutil.copy2(ROOT / "tools/templates/culinary-explorer.html",
                 SITE_DOCS / "culinary-explorer.html")
    files = build_assistant(index, SITE_DOCS, lambda commit, path: snapshot_bytes(ROOT, commit, path))
    target = SITE_DOCS / "recipe_assistant"
    target.mkdir()
    for name, data in files.items():
        (target / name).write_bytes(data)
    shutil.copy2(ROOT / "tools/templates/recipe-assistant.html", SITE_DOCS / "recipe-assistant.html")
    shutil.copy2(ROOT / "tools/templates/culinary-pantry.html", SITE_DOCS / "culinary-pantry.html")
    shutil.copy2(ROOT / "tools/templates/culinary-shopping.html", SITE_DOCS / "culinary-shopping.html")
    shutil.copy2(ROOT / "tools/templates/culinary-planner.html", SITE_DOCS / "culinary-planner.html")
    version_application_assets()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--without-explorer", action="store_true",
                        help="Preparar fuentes para auditoría sin regenerar el catálogo")
    args = parser.parse_args()
    if SITE_DOCS.exists():
        shutil.rmtree(SITE_DOCS)

    SITE_DOCS.mkdir()

    for item in INCLUDE:
        copy_item(item)


    create_index_files()
    normalize_links()
    create_home_page()
    if not args.without_explorer:
        build_explorer_page()

    print()
    print("NovaCoquinaria - Build")
    print("----------------------")
    print(f"Archivos copiados : {len(INCLUDE)}")
    print(f"Destino           : {SITE_DOCS}")
    print("Estado            : OK")


if __name__ == "__main__":
    main()