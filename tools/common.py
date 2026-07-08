from pathlib import Path
import re
from models import Document
import yaml


ROOT_DIR = Path(__file__).resolve().parents[1]

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "site",
    "site_docs",
    "__pycache__",
}

FRONTMATTER_REQUIRED_DIRS = {
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
    "docs/architecture",
}

FRONTMATTER_OPTIONAL_FILES = {
    "README.md",
    "CHANGELOG.md",
    "CONTEXT.md",
    "CONTRIBUTING.md",
    "ESPECIFICACION_DE_DOCUMENTOS.md",
    "GUIA_DE_ESTILO.md",
    "LICENSE.md",
    "MANIFESTO.md",
    "NovaCoquinaria.md",
    "tools/README.md",
    "tools/templates/home.md",
}

LINK_VALIDATION_EXCLUDED_DIRS = {
    "tools/templates",
}

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def iter_markdown_files():
    """Devuelve todos los archivos Markdown fuente del repositorio."""
    for path in ROOT_DIR.rglob("*.md"):
        relative_parts = path.relative_to(ROOT_DIR).parts

        if any(part in EXCLUDED_DIRS for part in relative_parts):
            continue

        yield path


def read_text(path: Path) -> str:
    """Lee un archivo Markdown como texto UTF-8."""
    return path.read_text(encoding="utf-8")


def extract_frontmatter(path: Path):
    """
    Extrae el Front Matter YAML de un documento Markdown.

    Devuelve:
    - dict si existe y es válido;
    - None si no existe;
    - lanza ValueError si el YAML es inválido.
    """
    text = read_text(path)
    match = FRONTMATTER_PATTERN.match(text)

    if not match:
        return None

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"Front Matter YAML inválido: {exc}") from exc

    return data or {}


def relative_path(path: Path) -> str:
    """Devuelve una ruta relativa al repositorio en formato POSIX."""
    return path.relative_to(ROOT_DIR).as_posix()


def print_error(path: Path, message: str):
    print(f"[ERROR] {relative_path(path)} :: {message}")


def print_warning(path: Path, message: str):
    print(f"[WARN]  {relative_path(path)} :: {message}")


def print_ok(message: str):
    print(f"[OK] {message}")


def load_documents():
    """
    Carga todos los documentos Markdown válidos del repositorio.
    """

    documents = []

    for path in iter_markdown_files():

        try:
            frontmatter = extract_frontmatter(path)
        except ValueError:
            continue

        if frontmatter is None:
            continue

        documents.append(
            Document(
                path=path,
                frontmatter=frontmatter,
                content=read_text(path),
            )
        )

    return documents


def requires_frontmatter(path: Path) -> bool:
    """Indica si un documento debe tener Front Matter obligatorio."""
    relative = relative_path(path)

    if relative in FRONTMATTER_OPTIONAL_FILES:
        return False
    
    if path.name == "BACKLOG.md":
        return False

    return any(
        relative == directory or relative.startswith(f"{directory}/")
        for directory in FRONTMATTER_REQUIRED_DIRS
    )