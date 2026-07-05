from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
SITE_DOCS = ROOT / "site_docs"

INCLUDE = [
    "README.md",
    "MANIFESTO.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE.md",
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

def copy_item(relative_path: str) -> None:
    src = ROOT / relative_path
    dst = SITE_DOCS / relative_path

    if not src.exists():
        print(f"SKIP: {relative_path}")
        return

    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("diagrams", "images", "templates"))
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

def main() -> None:
    if SITE_DOCS.exists():
        shutil.rmtree(SITE_DOCS)

    SITE_DOCS.mkdir()

    for item in INCLUDE:
        copy_item(item)

    shutil.copy2(SITE_DOCS / "README.md", SITE_DOCS / "index.md")

    print("site_docs generado correctamente.")

if __name__ == "__main__":
    main()