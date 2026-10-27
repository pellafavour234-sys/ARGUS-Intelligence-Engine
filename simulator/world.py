import random

from simulator.entities import (
    SimulatedEntity,
    create_entity,
)

from simulator.events import (
    SimulatedEvent,
    create_event,
)

from simulator.relationships import (
    SimulatedRelationship,
    create_relationship,
)


class SimulationWorld:

    def __init__(self, entity_count=500):

        self.entities = [
            create_entity(i)
            for i in range(entity_count)
        ]

        self.events: list[SimulatedEvent] = []
        self.relationships: list[
            SimulatedRelationship
        ] = []

    def generate_events(self, count=100):

        generated = []

        for _ in range(count):

            entity = random.choice(self.entities)

            event = create_event(entity.id)

            entity.interactions += 1
            entity.activity += event.value

            generated.append(event)

            self._maybe_create_relationship(entity)

        self.events.extend(generated)

        return generated

    def _maybe_create_relationship(self, entity):

        if random.random() > 0.35:
            return None

        target = random.choice(self.entities)

        if target.id == entity.id:
            return None

        relationship = create_relationship(
            entity.id,
            target.id,
        )

        self.relationships.append(
            relationship
        )

        return relationship

    def inject_behavioral_anomaly(
        self,
        entity,
        intensity=10.0,
    ):

        entity.activity *= intensity

        entity.interactions = int(
            max(
                1,
                entity.interactions * intensity,
            )
        )

    def snapshot(self):

        activities = [
            entity.activity
            for entity in self.entities
        ]

        return {
            "entities": len(self.entities),
            "events": len(self.events),
            "relationships": len(
                self.relationships
            ),
            "average_activity": (
                sum(activities)
                / max(len(activities), 1)
            ),
        }