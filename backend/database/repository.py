from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database.models import (
    Entity,
    Event,
    Relationship,
    Anomaly,
)


class Repository:

    def __init__(self, db: Session):
        self.db = db

    def save_entity(
        self,
        name,
        entity_type,
        activity=0.0,
        interactions=0,
    ):

        entity = Entity(
            name=name,
            entity_type=entity_type,
            activity_score=activity,
            interaction_count=interactions,
        )

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def get_entities(
        self,
        limit=100,
    ):

        statement = (
            select(Entity)
            .limit(limit)
        )

        return list(
            self.db.scalars(statement)
        )

    def save_event(
        self,
        entity_id,
        event_type,
        value,
        timestamp,
    ):

        event = Event(
            entity_id=entity_id,
            event_type=event_type,
            value=value,
            timestamp=timestamp,
        )

        self.db.add(event)

        return event

    def save_relationship(
        self,
        source_id,
        target_id,
        relationship_type,
        weight,
    ):

        relationship = Relationship(
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
            weight=weight,
        )

        self.db.add(relationship)

        return relationship

    def save_anomaly(
        self,
        entity_id,
        score,
        anomaly_type,
        explanation,
    ):

        anomaly = Anomaly(
            entity_id=entity_id,
            anomaly_score=score,
            anomaly_type=anomaly_type,
            explanation=explanation,
        )

        self.db.add(anomaly)
        self.db.commit()

        return anomaly