from enum import Enum


class Scenario(str, Enum):
    NORMAL = "normal"
    ACTIVITY_SPIKE = "activity_spike"
    BEHAVIOR_SHIFT = "behavior_shift"
    NETWORK_FORMATION = "network_formation"
    COORDINATED_ACTIVITY = "coordinated_activity"


class ScenarioEngine:

    def __init__(self, world):
        self.world = world

    def apply(self, scenario: Scenario):

        if scenario == Scenario.ACTIVITY_SPIKE:
            return self.activity_spike()

        if scenario == Scenario.BEHAVIOR_SHIFT:
            return self.behavior_shift()

        if scenario == Scenario.NETWORK_FORMATION:
            return self.network_formation()

        if scenario == Scenario.COORDINATED_ACTIVITY:
            return self.coordinated_activity()

        return {
            "scenario": Scenario.NORMAL,
            "affected": 0,
        }

    def activity_spike(self):

        affected = self.world.entities[:5]

        for entity in affected:
            self.world.inject_behavioral_anomaly(
                entity,
                intensity=8.0,
            )

        return {
            "scenario": "activity_spike",
            "affected": len(affected),
        }

    def behavior_shift(self):

        affected = self.world.entities[5:10]

        for entity in affected:
            entity.activity *= 4
            entity.interactions += 25

        return {
            "scenario": "behavior_shift",
            "affected": len(affected),
        }

    def network_formation(self):

        affected = self.world.entities[10:25]

        return {
            "scenario": "network_formation",
            "affected": len(affected),
        }

    def coordinated_activity(self):

        affected = self.world.entities[25:35]

        for entity in affected:
            entity.activity *= 3
            entity.interactions += 15

        return {
            "scenario": "coordinated_activity",
            "affected": len(affected),
        }