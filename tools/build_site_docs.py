from pathlib import Path
import shutil

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
    "04_Verduras",
    "05_Carnes",
    "06_Pescados_y_Mariscos",
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


def main() -> None:
    if SITE_DOCS.exists():
        shutil.rmtree(SITE_DOCS)

    SITE_DOCS.mkdir()

    for item in INCLUDE:
        copy_item(item)


    create_index_files()
    normalize_links()
    create_home_page()

    print()
    print("NovaCoquinaria - Build")
    print("----------------------")
    print(f"Archivos copiados : {len(INCLUDE)}")
    print(f"Destino           : {SITE_DOCS}")
    print("Estado            : OK")


if __name__ == "__main__":
    main()