from simulator.world import (
    SimulationWorld,
)

from simulator.scenarios import (
    Scenario,
    ScenarioEngine,
)


class SimulationService:

    def __init__(
        self,
        entity_count=500,
    ):

        self.world = SimulationWorld(
            entity_count
        )

        self.scenarios = (
            ScenarioEngine(
                self.world
            )
        )

    def generate(
        self,
        count=100,
    ):

        events = (
            self.world.generate_events(
                count
            )
        )

        return {
            "generated":
                len(events),

            "snapshot":
                self.world.snapshot(),
        }

    def run_scenario(
        self,
        scenario: str,
    ):

        selected = Scenario(
            scenario
        )

        return self.scenarios.apply(
            selected
        )

    def get_world(self):

        return self.world