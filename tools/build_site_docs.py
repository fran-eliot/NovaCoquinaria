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
    "GUIA_DE_ESTILO.md",
    "ESPECIFICACION_DE_DOCUMENTOS.md",
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
        "README": "index",  
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


def create_home_page() -> None:
    content = """# 🍳 NovaCoquinaria

> Sistema de Gestión del Conocimiento Culinario.

NovaCoquinaria no es solo un recetario. Es una base de conocimiento culinario construida con principios de arquitectura documental, reutilización y mejora continua.

## Explorar

<div class="grid cards" markdown>

-   :material-book-open-page-variant: **Bases**

    ---

    Técnicas, fundamentos y conocimiento culinario reutilizable.

    [:octicons-arrow-right-24: Explorar bases](00_Bases/)

-   :material-food-apple: **Despensa**

    ---

    Ingredientes, salsas, aceites, condimentos y productos clave.

    [:octicons-arrow-right-24: Explorar despensa](11_Despensa/)

-   :material-shape-outline: **Plantillas**

    ---

    Patrones reutilizables para crear recetas sin duplicar conocimiento.

    [:octicons-arrow-right-24: Explorar plantillas](12_Plantillas/)

-   :material-silverware-fork-knife: **Recetas**

    ---

    Elaboraciones normalizadas conectadas con técnicas, ingredientes y tablas.

    [:octicons-arrow-right-24: Ver recetas](01_Arroces/arroz_chaufa.md)

-   :material-table: **Tablas**

    ---

    Tiempos, conversiones, conservación, seguridad alimentaria y sustituciones.

    [:octicons-arrow-right-24: Consultar tablas](98_Tablas/)

-   :material-sitemap: **Arquitectura**

    ---

    Visión, decisiones arquitectónicas, roadmap y calidad documental.

    [:octicons-arrow-right-24: Ver arquitectura](docs/ARQUITECTURA.md)

</div>

## Filosofía

El conocimiento se documenta una sola vez y se reutiliza mediante referencias.

Las recetas no repiten explicaciones generales: orquestan técnicas, ingredientes, plantillas y tablas existentes.

## Estado

NovaCoquinaria dispone de una base inicial estable formada por:

- fundamentos culinarios;
- tablas de referencia;
- despensa estructurada;
- plantillas reutilizables;
- recetas normalizadas;
- documentación arquitectónica.

"""
    (SITE_DOCS / "index.md").write_text(content, encoding="utf-8")


def main() -> None:
    if SITE_DOCS.exists():
        shutil.rmtree(SITE_DOCS)

    SITE_DOCS.mkdir()

    for item in INCLUDE:
        copy_item(item)

    shutil.copy2(SITE_DOCS / "README.md", SITE_DOCS / "index.md")


    create_index_files()
    normalize_links()
    create_home_page()

    print("site_docs generado correctamente.")


if __name__ == "__main__":
    main()