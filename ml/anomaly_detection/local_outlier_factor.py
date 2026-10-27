from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler

from ml.preprocessing.feature_engineering import (
    FEATURE_COLUMNS,
)


class LOFDetector:

    def __init__(
        self,
        contamination=0.05,
        neighbors=20,
    ):

        self.scaler = StandardScaler()

        self.model = LocalOutlierFactor(
            n_neighbors=neighbors,
            contamination=contamination,
            novelty=True,
        )

        self._fitted = False

    def fit(self, dataframe):

        X = dataframe[
            FEATURE_COLUMNS
        ]

        X_scaled = self.scaler.fit_transform(X)

        self.model.fit(X_scaled)

        self._fitted = True

        return self

    def predict(self, dataframe):

        if not self._fitted:
            raise RuntimeError(
                "LOF detector has not been fitted."
            )

        X = dataframe[
            FEATURE_COLUMNS
        ]

        X_scaled = self.scaler.transform(X)

        predictions = self.model.predict(
            X_scaled
        )

        scores = -self.model.decision_function(
            X_scaled
        )

        min_score = scores.min()
        max_score = scores.max()

        normalized = (
            (scores - min_score)
            /
            (max_score - min_score + 1e-9)
        )

        return [
            {
                "entity_id": entity_id,
                "score": float(score),
                "is_anomaly": prediction == -1,
            }
            for entity_id, score, prediction
            in zip(
                dataframe["entity_id"],
                normalized,
                predictions,
            )
        ]