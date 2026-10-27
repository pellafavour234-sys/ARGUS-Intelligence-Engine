import networkx as nx


class GraphFeatureEngine:

    def __init__(self, graph):
        self.graph = graph

    def degree_features(self):

        return dict(
            self.graph.degree()
        )

    def centrality_features(self):

        return nx.degree_centrality(
            self.graph
        )

    def betweenness_features(self):

        return nx.betweenness_centrality(
            self.graph,
            normalized=True,
        )

    def clustering_features(self):

        return nx.clustering(
            self.graph
        )

    def node_features(self):

        degree = self.degree_features()

        centrality = (
            self.centrality_features()
        )

        betweenness = (
            self.betweenness_features()
        )

        clustering = (
            self.clustering_features()
        )

        nodes = self.graph.nodes()

        return {
            node: {
                "degree":
                    degree.get(node, 0),

                "centrality":
                    centrality.get(node, 0),

                "betweenness":
                    betweenness.get(node, 0),

                "clustering":
                    clustering.get(node, 0),
            }
            for node in nodes
        }