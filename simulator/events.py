from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


EVENT_TYPES = (
    "INTERACTION",
    "LOCATION_CHANGE",
    "DEVICE_ACCESS",
    "TRANSACTION",
)


@dataclass(slots=True)
class SimulatedEvent:
    id: str
    entity_id: str
    event_type: str
    value: float
    timestamp: datetime


def create_event(entity_id: str) -> SimulatedEvent:
    import random

    return SimulatedEvent(
        id=str(uuid4()),
        entity_id=entity_id,
        event_type=random.choice(EVENT_TYPES),
        value=round(random.uniform(0.1, 100.0), 2),
        timestamp=datetime.now(timezone.utc),
    )