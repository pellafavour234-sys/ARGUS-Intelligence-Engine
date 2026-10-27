from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_entities():

    return {
        "items": [],
        "total": 0,
    }