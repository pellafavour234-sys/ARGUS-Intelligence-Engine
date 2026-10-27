import networkx as nx


class GraphAnalyzer:

    def __init__(self, graph):
        self.graph = graph

    def communities(self):

        if self.graph.number_of_nodes() == 0:
            return []

        communities = (
            nx.community.greedy_modularity_communities(
                self.graph
            )
        )

        return [
            list(community)
            for community in communities
        ]

    def important_nodes(self, limit=10):

        centrality = (
            nx.degree_centrality(
                self.graph
            )
        )

        return sorted(
            centrality.items(),
            key=lambda item: item[1],
            reverse=True,
        )[:limit]

    def shortest_path(
        self,
        source,
        target,
    ):

        if not nx.has_path(
            self.graph,
            source,
            target,
        ):
            return None

        return nx.shortest_path(
            self.graph,
            source,
            target,
        )