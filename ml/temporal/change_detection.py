import numpy as np


class BehavioralChangeDetector:

    def __init__(
        self,
        threshold=2.5,
    ):

        self.threshold = threshold

    def compare(
        self,
        previous,
        current,
    ):

        previous = np.asarray(
            previous,
            dtype=float,
        )

        current = np.asarray(
            current,
            dtype=float,
        )

        mean = previous.mean()

        std = previous.std()

        if std == 0:
            std = 1e-9

        z_scores = (
            current - mean
        ) / std

        changes = np.abs(
            z_scores
        ) >= self.threshold

        return {
            "z_scores":
                z_scores.tolist(),

            "changed":
                changes.tolist(),

            "change_count":
                int(changes.sum()),
        }