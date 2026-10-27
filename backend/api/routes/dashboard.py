from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def dashboard():

    return {
        "system": "ARGUS",
        "status": "operational",
        "entities": 0,
        "relationships": 0,
        "events": 0,
        "anomalies": 0,
        "model_status": "ready",
    }