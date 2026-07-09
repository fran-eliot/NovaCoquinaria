from collections import Counter

from common import ROOT_DIR, print_ok
from generate_graph import build_graph

OUTPUT_FILE = ROOT_DIR / "docs" / "diagrams" / "knowledge_graph_stats.md"


def generate_markdown_report(graph, by_type, incoming_count, most_referenced, reusable_orphans):
    lines = [
        "# Estadísticas del Knowledge Graph",
        "",
        "> Informe generado automáticamente a partir del grafo documental de NovaCoquinaria.",
        "",
        "## Resumen",
        "",
        f"- Nodos: {graph.node_count}",
        f"- Relaciones: {graph.edge_count}",
        "",
        "## Documentos por tipo",
        "",
        "| Tipo | Total |",
        "|---|---:|",
    ]

    for tipo, total in sorted(by_type.items()):
        lines.append(f"| {tipo} | {total} |")

    lines.extend([
        "",
        "## Documentos más referenciados",
        "",
        "| ID | Tipo | Documento | Referencias |",
        "|---|---|---|---:|",
    ])

    for document in most_referenced[:10]:
        count = incoming_count[document.graph_id]

        if count == 0:
            continue

        lines.append(
            f"| {document.id} | {document.tipo} | "
            f"{document.graph_label} | {count} |"
        )

    lines.extend([
        "",
        "## Conocimiento reutilizable huérfano",
        "",
    ])

    if reusable_orphans:
        lines.extend([
            "| ID | Tipo | Documento |",
            "|---|---|---|",
        ])

        for document in sorted(
            reusable_orphans,
            key=lambda d: (d.tipo or "", d.graph_label),
        ):
            lines.append(
                f"| {document.id} | {document.tipo} | {document.graph_label} |"
            )
    else:
        lines.append("No se ha detectado conocimiento reutilizable huérfano.")

    lines.append("")
    return "\n".join(lines)


def generate_graph_stats():
    graph = build_graph()

    by_type = Counter(
        document.tipo or "sin_tipo"
        for document in graph.nodes.values()
    )

    incoming_count = {
        node_id: len(graph.incoming(node_id))
        for node_id in graph.nodes
    }

    most_referenced = sorted(
        graph.nodes.values(),
        key=lambda document: incoming_count[document.graph_id],
        reverse=True,
    )

    reusable_orphans = [
        document
        for document in graph.nodes.values()
        if document.tipo not in {"receta", "arquitectura"}
        and incoming_count[document.graph_id] == 0
    ]

    print()
    print("NovaCoquinaria - Estadísticas del grafo")
    print("--------------------------------------")
    print(f"Nodos      : {graph.node_count}")
    print(f"Relaciones : {graph.edge_count}")

    print()
    print("Documentos por tipo:")
    for tipo, total in sorted(by_type.items()):
        print(f"- {tipo}: {total}")

    print()
    print("Documentos más referenciados:")
    for document in most_referenced[:10]:
        count = incoming_count[document.graph_id]

        if count == 0:
            continue

        print(
            f"- {document.id} | {document.tipo} | "
            f"{document.graph_label} | {count} referencia(s)"
        )

    print()
    print("Conocimiento reutilizable huérfano:")
    if reusable_orphans:
        for document in sorted(
            reusable_orphans,
            key=lambda d: (d.tipo or "", d.graph_label),
        ):
            print(
                f"- {document.id} | {document.tipo} | "
                f"{document.graph_label}"
            )
    else:
        print("- Ninguno")

    print()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        generate_markdown_report(
            graph,
            by_type,
            incoming_count,
            most_referenced,
            reusable_orphans,
        ),
        encoding="utf-8",
    )
    print_ok(
        f"Estadísticas del grafo generadas: "
        f"{OUTPUT_FILE.relative_to(ROOT_DIR).as_posix()}"
    )
    return 0



if __name__ == "__main__":
    raise SystemExit(generate_graph_stats())