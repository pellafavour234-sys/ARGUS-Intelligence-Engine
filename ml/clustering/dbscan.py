from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from ml.preprocessing.feature_engineering import (
    FEATURE_COLUMNS,
)


class DensityClusterer:

    def __init__(
        self,
        eps=0.8,
        min_samples=5,
    ):

        self.scaler = StandardScaler()

        self.model = DBSCAN(
            eps=eps,
            min_samples=min_samples,
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