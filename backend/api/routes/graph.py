from fastapi import APIRouter

from backend.database.database import SessionLocal
from backend.database.models import (
    Entity,
    Relationship,
)

router = APIRouter()


@router.get("/")
def get_graph():

    db = SessionLocal()

    try:

        entities = db.query(
            Entity
        ).limit(500).all()

        relationships = db.query(
            Relationship
        ).limit(1000).all()

        nodes = [
            {
                "id": entity.id,
                "name": entity.name,
                "type": entity.entity_type,
            }
            for entity in entities
        ]

        links = [
            {
                "source":
                    relationship.source_id,

                "target":
                    relationship.target_id,

                "type":
                    relationship.relationship_type,

                "weight":
                    relationship.weight,
            }
            for relationship in relationships
        ]

        return {
            "nodes": nodes,
            "links": links,
        }

    finally:
        db.close()