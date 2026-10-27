import numpy as np
import pandas as pd


FEATURE_COLUMNS = [
    "activity",
    "interactions",
    "activity_per_interaction",
]


def build_entity_features(entities) -> pd.DataFrame:

    rows = []

    for entity in entities:

        interactions = max(entity.interactions, 1)

        rows.append(
            {
                "entity_id": entity.id,
                "activity": entity.activity,
                "interactions": entity.interactions,
                "activity_per_interaction": (
                    entity.activity / interactions
                ),
            }
        )

    frame = pd.DataFrame(rows)

    if frame.empty:
        return frame

    frame[FEATURE_COLUMNS] = (
        frame[FEATURE_COLUMNS]
        .replace([np.inf, -np.inf], np.nan)
        .fillna(0.0)
    )

    return frame