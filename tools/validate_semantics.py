from generate_graph import build_graph
from common import ROOT_DIR, print_ok, print_warning


EXPECTED_OUTGOING_TYPES = {
    "receta": {
        "base",
        "tecnica",
        "ingrediente",
        "plantilla",
        "tabla",
    },
    "plantilla": {
        "base",
        "tecnica",
        "ingrediente",
        "tabla",
    },
    "tecnica": {
        "tabla",
        "ingrediente",
        "base",
    },
}


def outgoing_documents(graph, document):
    return [
        graph.nodes[target_id]
        for target_id in graph.neighbours(document.graph_id)
        if target_id in graph.nodes
    ]


def validate_semantics():
    graph = build_graph()
    warnings = 0

    print()
    print("NovaCoquinaria - Validación semántica")
    print("------------------------------------")

    for document in sorted(
        graph.nodes.values(),
        key=lambda d: (d.tipo or "", d.graph_label),
    ):
        expected_types = EXPECTED_OUTGOING_TYPES.get(document.tipo)

        if not expected_types:
            continue

        outgoing = outgoing_documents(graph, document)
        outgoing_types = {
            target.tipo
            for target in outgoing
            if target.tipo
        }

        if not outgoing:
            print_warning(
                ROOT_DIR / document.path,
                f"{document.id} no referencia ningún documento",
            )
            warnings += 1
            continue

        if not outgoing_types.intersection(expected_types):
            print_warning(
                ROOT_DIR / document.path,
                f"{document.id} no reutiliza conocimiento esperado "
                f"({', '.join(sorted(expected_types))})",
            )
            warnings += 1

    if warnings:
        print()
        print(f"Validación semántica finalizada con {warnings} advertencia(s).")
        return 0

    print_ok("Validación semántica sin advertencias.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate_semantics())