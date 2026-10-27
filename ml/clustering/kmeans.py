from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from ml.preprocessing.feature_engineering import (
    FEATURE_COLUMNS,
)


class BehavioralClusterer:

    def __init__(
        self,
        clusters=5,
        random_state=42,
    ):

        self.scaler = StandardScaler()

        self.model = KMeans(
            n_clusters=clusters,
            n_init=20,
            random_state=random_state,
        )

    def fit_predict(self, dataframe):

        X = dataframe[
            FEATURE_COLUMNS
        ]

        X_scaled = self.scaler.fit_transform(X)

        labels = self.model.fit_predict(
            X_scaled
        )

        result = dataframe[
            ["entity_id"]
        ].copy()

        result["cluster"] = labels

        return result