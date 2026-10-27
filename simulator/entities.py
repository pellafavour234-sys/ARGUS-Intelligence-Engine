from dataclasses import dataclass
from uuid import uuid4


ENTITY_TYPES = (
    "PERSON",
    "ORGANIZATION",
    "DEVICE",
    "LOCATION",
)


@dataclass(slots=True)
class SimulatedEntity:
    id: str
    name: str
    entity_type: str
    activity: float = 0.0
    interactions: int = 0


def create_entity(index: int) -> SimulatedEntity:
    entity_type = ENTITY_TYPES[index % len(ENTITY_TYPES)]

    return SimulatedEntity(
        id=str(uuid4()),
        name=f"{entity_type}_{index:05d}",
        entity_type=entity_type,
    )