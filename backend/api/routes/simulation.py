from fastapi import APIRouter

from simulator.world import SimulationWorld

router = APIRouter()

world = SimulationWorld(entity_count=500)


@router.post("/generate")
def generate_events(count: int = 100):

    events = world.generate_events(count)

    return {
        "generated": len(events),
        "world": world.snapshot(),
    }