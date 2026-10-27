from simulator.world import SimulationWorld

from ml.preprocessing.feature_engineering import (
    build_entity_features,
)

from ml.anomaly_detection.ensemble_detector import (
    EnsembleAnomalyDetector,
)


def test_detector():

    world = SimulationWorld(
        entity_count=100
    )

    world.generate_events(
        1000
    )

    dataframe = (
        build_entity_features(
            world.entities
        )
    )

    detector = (
        EnsembleAnomalyDetector()
    )

    detector.fit(
        dataframe
    )

    results = detector.predict(
        dataframe
    )

    assert len(results) == 100

    assert all(
        "anomaly_score" in result
        for result in results
    )