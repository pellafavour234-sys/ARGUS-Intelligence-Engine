from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Entity(Base):
    __tablename__ = "entities"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    name: Mapped[str] = mapped_column(
        String(150),
        index=True,
    )

    entity_type: Mapped[str] = mapped_column(
        String(50),
        index=True,
    )

    activity_score: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    interaction_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="active",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
    )


class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    entity_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    event_type: Mapped[str] = mapped_column(
        String(50),
        index=True,
    )

    value: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        index=True,
    )


class Relationship(Base):
    __tablename__ = "relationships"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    source_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    target_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    relationship_type: Mapped[str] = mapped_column(
        String(50),
    )

    weight: Mapped[float] = mapped_column(
        Float,
        default=1.0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
    )


class Anomaly(Base):
    __tablename__ = "anomalies"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    entity_id: Mapped[str] = mapped_column(
        String(36),
        index=True,
    )

    anomaly_score: Mapped[float] = mapped_column(
        Float,
    )

    anomaly_type: Mapped[str] = mapped_column(
        String(50),
    )

    explanation: Mapped[str] = mapped_column(
        Text,
    )

    detected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
    )