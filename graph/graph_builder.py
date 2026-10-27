import networkx as nx


class IntelligenceGraph:

    def __init__(self):
        self.graph = nx.Graph()

    def add_entity(
        self,
        entity_id: str,
        entity_type: str,
        name: str,
    ):

        self.graph.add_node(
            entity_id,
            entity_type=entity_type,
            name=name,
        )

    def add_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
        weight: float = 1.0,
    ):

        self.graph.add_edge(
            source_id,
            target_id,
            relationship_type=relationship_type,
            weight=weight,
        )

    def get_statistics(self) -> dict:

        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "density": nx.density(self.graph),
        }

    def centrality(self) -> dict:

        return nx.degree_centrality(self.graph)