from collections import defaultdict

from common import (
    load_documents,
    print_error,
    print_ok,
)


def validate_ids():
    ids = defaultdict(list)
    errors = 0

    for document in load_documents():

        if document.id:
            ids[document.id].append(document.path)

    for document_id, paths in sorted(ids.items()):
        if len(paths) > 1:
            errors += 1
            print(f"\nID duplicado: {document_id}")

            for path in paths:
                print_error(path, "Identificador duplicado")

    if errors:
        print(f"\nSe encontraron {errors} identificador(es) duplicado(s).")
        return 1

    print_ok(f"{len(ids)} identificadores únicos verificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate_ids())