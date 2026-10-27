from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

import random


RELATIONSHIP_TYPES = (
    "WORKS_WITH",
    "CONNECTED_TO",
    "LOCATED_NEAR",
    "OWNS",
    "PARTNERED_WITH",
    "COMMUNICATES_WITH",
)


@dataclass(slots=True)
class SimulatedRelationship:
    id: str
    source_id: str
    target_id: str
    relationship_type: str
    weight: float
    timestamp: datetime


def create_relationship(source_id, target_id):
    return SimulatedRelationship(
        id=str(uuid4()),
        source_id=source_id,
        target_id=target_id,
        relationship_type=random.choice(
            RELATIONSHIP_TYPES
        ),
        weight=round(
            random.uniform(0.1, 1.0),
            3
        ),
        timestamp=datetime.now(timezone.utc),
    )