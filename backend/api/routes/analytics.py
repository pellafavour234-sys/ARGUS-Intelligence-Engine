from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
def analytics_summary():

    return {
        "anomaly_detection": {
            "model": "ensemble",
            "components": [
                "IsolationForest",
                "LocalOutlierFactor",
            ],
        },

        "clustering": {
            "algorithms": [
                "KMeans",
                "DBSCAN",
            ],
        },

        "graph": {
            "algorithms": [
                "DegreeCentrality",
                "BetweennessCentrality",
                "CommunityDetection",
            ],
        },

        "temporal": {
            "method": "ZScoreChangeDetection",
        },
    }