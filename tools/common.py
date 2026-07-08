from pathlib import Path
import re
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