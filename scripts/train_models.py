from simulator.world import SimulationWorld

from ml.preprocessing.feature_engineering import (
    build_entity_features,
)

from ml.anomaly_detection.ensemble_detector import (
    EnsembleAnomalyDetector,
)


def main():

    print(
        "\nARGUS MODEL TRAINING\n"
        "====================\n"
    )

    world = SimulationWorld(
        entity_count=1000
    )

    world.generate_events(
        count=10000
    )

    features = (
        build_entity_features(
            world.entities
        )
    )

    detector = (
        EnsembleAnomalyDetector(
            contamination=0.05
        )
    )

    detector.fit(features)

    results = detector.predict(
        features
    )

    anomalies = [
        result
        for result in results
        if result["is_anomaly"]
    ]

    print(
        f"Entities analysed: "
        f"{len(features)}"
    )

    print(
        f"Anomalies detected: "
        f"{len(anomalies)}"
    )


if __name__ == "__main__":
    main()