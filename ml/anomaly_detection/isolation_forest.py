from dataclasses import dataclass

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

from ml.preprocessing.feature_engineering import (
    FEATURE_COLUMNS,
)


@dataclass
class AnomalyResult:
    entity_id: str
    score: float
    is_anomaly: bool


class IsolationForestDetector:

    def __init__(
        self,
        contamination: float = 0.05,
        random_state: int = 42,
    ):
        self.scaler = StandardScaler()

        self.model = IsolationForest(
            n_estimators=300,
            contamination=contamination,
            max_samples="auto",
            random_state=random_state,
            n_jobs=-1,
        )

        self._fitted = False

    def fit(self, dataframe):
        features = dataframe[FEATURE_COLUMNS]

        scaled = self.scaler.fit_transform(features)

        self.model.fit(scaled)

        self._fitted = True

        return self

    def predict(self, dataframe):

        if not self._fitted:
            raise RuntimeError(
                "Detector must be fitted before prediction."
            )

        features = dataframe[FEATURE_COLUMNS]

        scaled = self.scaler.transform(features)

        predictions = self.model.predict(scaled)

        raw_scores = self.model.decision_function(scaled)

        # Convert Isolation Forest scores into
        # an easier-to-understand anomaly scale.
        normalized_scores = 1 - (
            (raw_scores - raw_scores.min())
            / (
                raw_scores.max()
                - raw_scores.min()
                + 1e-9
            )
        )

        results = []

        for entity_id, prediction, score in zip(
            dataframe["entity_id"],
            predictions,
            normalized_scores,
        ):

            results.append(
                AnomalyResult(
                    entity_id=entity_id,
                    score=float(np.clip(score, 0, 1)),
                    is_anomaly=prediction == -1,
                )
            )

        return results