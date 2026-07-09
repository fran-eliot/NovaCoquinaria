from dataclasses import dataclass, field


@dataclass(slots=True)
class KnowledgeGraph:
    """
    Grafo de conocimiento de NovaCoquinaria.

    Cada nodo representa un documento Markdown.
    Cada arista representa una referencia mediante enlace Markdown.
    """

    nodes: set[str] = field(default_factory=set)
    edges: dict[str, set[str]] = field(default_factory=dict)

    def add_node(self, node: str):
        self.nodes.add(node)
        self.edges.setdefault(node, set())

    def add_edge(self, source: str, target: str):
        self.add_node(source)
        self.add_node(target)
        self.edges[source].add(target)

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