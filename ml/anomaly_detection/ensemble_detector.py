import numpy as np

from ml.anomaly_detection.isolation_forest import (
    IsolationForestDetector,
)

from ml.anomaly_detection.local_outlier_factor import (
    LOFDetector,
)


class EnsembleAnomalyDetector:

    def __init__(
        self,
        contamination=0.05,
    ):

        self.isolation_forest = (
            IsolationForestDetector(
                contamination=contamination
            )
        )

        self.lof = LOFDetector(
            contamination=contamination
        )

        self.fitted = False

    def fit(self, dataframe):

        self.isolation_forest.fit(
            dataframe
        )

        self.lof.fit(dataframe)

        self.fitted = True

        return self

    def predict(self, dataframe):

        if not self.fitted:
            raise RuntimeError(
                "Ensemble must be fitted first."
            )

        isolation_results = (
            self.isolation_forest.predict(
                dataframe
            )
        )

        lof_results = (
            self.lof.predict(dataframe)
        )

        results = []

        for isolation, lof in zip(
            isolation_results,
            lof_results,
        ):

            score = (
                isolation.score * 0.6
                +
                lof["score"] * 0.4
            )

            is_anomaly = (
                isolation.is_anomaly
                or lof["is_anomaly"]
            )

            results.append(
                {
                    "entity_id":
                        isolation.entity_id,

                    "anomaly_score":
                        float(
                            np.clip(
                                score,
                                0,
                                1,
                            )
                        ),

                    "is_anomaly":
                        bool(is_anomaly),
                }
            )

        return results