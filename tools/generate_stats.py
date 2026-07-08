from collections import Counter

from common import (
    load_documents,
    print_ok,
)


def generate_stats():
    documents = load_documents()

    by_type = Counter(document.tipo or "sin_tipo" for document in documents)

    print()
    print("NovaCoquinaria - Estadísticas")
    print("-----------------------------")
    print(f"Documentos con Front Matter : {len(documents)}")
    print()

    print("Por tipo:")
    for tipo, total in sorted(by_type.items()):
        print(f"- {tipo}: {total}")

    print()
    print_ok("Estadísticas generadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(generate_stats())