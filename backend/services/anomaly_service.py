from ml.preprocessing.feature_engineering import (
    build_entity_features,
)

from ml.anomaly_detection.ensemble_detector import (
    EnsembleAnomalyDetector,
)


class AnomalyService:

    def __init__(self):

        self.detector = (
            EnsembleAnomalyDetector(
                contamination=0.05
            )
        )

    def analyze(self, entities):

        dataframe = build_entity_features(
            entities
        )

        if len(dataframe) < 10:
            return []

        self.detector.fit(
            dataframe
        )

        return self.detector.predict(
            dataframe
        )