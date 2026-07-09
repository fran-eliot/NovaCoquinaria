from generate_graph import build_graph
from common import print_ok


IGNORED_ORPHAN_TYPES = {
    "arquitectura",
    "receta",
}


def find_orphans():
    graph = build_graph()

    orphan_ids = graph.orphan_nodes()

    orphans = [
        graph.nodes[orphan_id]
        for orphan_id in orphan_ids
        if graph.nodes[orphan_id].tipo not in IGNORED_ORPHAN_TYPES
    ]

    print()
    print("NovaCoquinaria - Documentos huérfanos")
    print("------------------------------------")

    if not orphans:
        print_ok("No se encontraron documentos huérfanos.")
        return 0

    for document in sorted(orphans, key=lambda d: (d.tipo or "", d.graph_label)):
        print(
            f"- {document.id} | {document.tipo} | "
            f"{document.graph_label} | {document.relative_path}"
        )

    print()
    print(f"Total: {len(orphans)} documento(s) huérfano(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(find_orphans())