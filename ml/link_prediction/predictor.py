import networkx as nx


class LinkPredictor:

    def __init__(self, graph):
        self.graph = graph

    def predict(
        self,
        top_k=20,
    ):

        candidates = nx.jaccard_coefficient(
            self.graph
        )

        predictions = []

        for source, target, score in candidates:

            predictions.append(
                {
                    "source": source,
                    "target": target,
                    "score": float(score),
                }
            )

        predictions.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return predictions[:top_k]