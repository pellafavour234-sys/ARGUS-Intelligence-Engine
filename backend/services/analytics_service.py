from ml.clustering.kmeans import (
    BehavioralClusterer,
)

from ml.clustering.dbscan import (
    DensityClusterer,
)

from ml.preprocessing.feature_engineering import (
    build_entity_features,
)


class AnalyticsService:

    def analyze(self, entities):

        dataframe = (
            build_entity_features(
                entities
            )
        )

        if len(dataframe) < 10:
            return {
                "clusters": [],
                "density_clusters": [],
            }

        kmeans = BehavioralClusterer(
            clusters=5
        )

        dbscan = DensityClusterer()

        kmeans_result = (
            kmeans.fit_predict(
                dataframe
            )
        )

        dbscan_result = (
            dbscan.fit_predict(
                dataframe
            )
        )

        return {
            "clusters":
                kmeans_result.to_dict(
                    orient="records"
                ),

            "density_clusters":
                dbscan_result.to_dict(
                    orient="records"
                ),
        }