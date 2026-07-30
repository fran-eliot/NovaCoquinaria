from collections import defaultdict
from pathlib import Path

from common import (
    extract_frontmatter,
    iter_markdown_files,
    print_error,
    print_ok,
)


def validate_ids() -> int:
    """
    Comprueba que los identificadores declarados en el Front Matter
    sean únicos en todo el repositorio.
    """
    documents_by_id: dict[str, list[Path]] = defaultdict(list)

    errors = 0
    checked_documents = 0
    documents_with_id = 0

    for path in iter_markdown_files():
        checked_documents += 1

        try:
            metadata = extract_frontmatter(path)
        except ValueError as exc:
            print_error(path, str(exc))
            errors += 1
            continue

        # Algunos documentos Markdown no requieren Front Matter.
        if metadata is None:
            continue

        document_id = metadata.get("id")

        # La ausencia de ID corresponde al validador de Front Matter.
        if not document_id:
            continue

        if not isinstance(document_id, str):
            print_error(path, "El identificador debe ser una cadena de texto")
            errors += 1
            continue

        document_id = document_id.strip()

        if not document_id:
            print_error(path, "El identificador no puede estar vacío")
            errors += 1
            continue

        documents_by_id[document_id].append(path)
        documents_with_id += 1

    for document_id, paths in sorted(documents_by_id.items()):
        if len(paths) <= 1:
            continue

        print(f"\nID duplicado: {document_id}")

        for path in paths:
            print_error(
                path,
                f"Identificador duplicado: {document_id}",
            )
            errors += 1

    if errors:
        print(
            f"\nValidación finalizada con {errors} error(es) "
            f"en {checked_documents} documento(s)."
        )
        return 1

    print_ok(
        f"{documents_with_id} identificador(es) único(s) "
        f"verificados en {checked_documents} documento(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(validate_ids())