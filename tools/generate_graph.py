from pathlib import Path

from common import (
    ROOT_DIR,
    load_documents,
    print_ok,
)
from graph import KnowledgeGraph
from models import Document


OUTPUT_FILE = ROOT_DIR / "docs" / "diagrams" / "knowledge_graph.mmd"


def build_document_index(documents):
    return {
        (ROOT_DIR / document.path).resolve(): document
        for document in documents
    }


def resolve_link(document, link: str):
    target_path = (ROOT_DIR / document.path.parent / link).resolve()
    return target_path


def build_graph():
    documents = load_documents()
    document_index = build_document_index(documents)

    graph = KnowledgeGraph()

    for document in documents:
        graph.add_node(document)

        for link in document.links:
            target_path = resolve_link(document, link)
            target_document = document_index.get(target_path)

            if target_document:
                graph.add_edge(document, target_document)

    return graph


def mermaid_node_id(document: Document) -> str:
    return document.graph_id


def generate_mermaid(graph: KnowledgeGraph) -> str:
    lines = [
        "graph TD",
        "",
    ]

    for document in sorted(
        graph.nodes.values(),
        key=lambda d: d.graph_id,
    ):
        node_id = mermaid_node_id(document)

        label = f"{document.id}\n{document.graph_label}"

        lines.append(
            f'{node_id}["{label}"]'
        )

    lines.append("")

    for source_id, targets in sorted(graph.edges.items()):

        source_node = mermaid_node_id(graph.nodes.get(source_id))

        for target_id in sorted(targets):

            target_node = mermaid_node_id(graph.nodes.get(target_id))

            lines.append(
                f"    {source_node} --> {target_node}"
            )

    lines.append("")
    return "\n".join(lines)


def main():
    graph = build_graph()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(generate_mermaid(graph), encoding="utf-8")

    print_ok(
        f"Grafo generado: {OUTPUT_FILE.relative_to(ROOT_DIR).as_posix()} "
        f"({graph.node_count} nodos, {graph.edge_count} aristas)"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())