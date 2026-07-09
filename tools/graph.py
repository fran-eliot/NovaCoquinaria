from dataclasses import dataclass, field

from models import Document


@dataclass(slots=True)
class KnowledgeGraph:
    """
    Grafo de conocimiento de NovaCoquinaria.

    Cada nodo representa un documento Markdown.
    Cada arista representa una referencia mediante enlace Markdown.
    """

    nodes: dict[str, Document] = field(default_factory=dict)
    edges: dict[str, set[str]] = field(default_factory=dict)

    def add_node(self, document: Document):
        self.nodes[document.graph_id] = document
        self.edges.setdefault(document.graph_id, set())

    def add_edge(self, source: Document, target: Document):
        self.add_node(source)
        self.add_node(target)

        self.edges[source.graph_id].add(target.graph_id)

    def neighbours(self, node: str) -> set[str]:
        return self.edges.get(node, set())

    def incoming(self, node: str) -> set[str]:
        incoming = set()

        for source, targets in self.edges.items():
            if node in targets:
                incoming.add(source)

        return incoming

    def orphan_nodes(self) -> set[str]:
        """
        Devuelve los documentos sin referencias entrantes.
        """
        return {
            node
            for node in self.nodes
            if len(self.incoming(node)) == 0
        }

    @property
    def node_count(self) -> int:
        return len(self.nodes)

    @property
    def edge_count(self) -> int:
        return sum(len(targets) for targets in self.edges.values())