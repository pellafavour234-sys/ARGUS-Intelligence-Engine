from simulator.world import SimulationWorld


def test_world_creates_entities():

    world = SimulationWorld(
        entity_count=100
    )

    assert len(
        world.entities
    ) == 100


def test_event_generation():

    world = SimulationWorld(
        entity_count=100
    )

    events = world.generate_events(
        50
    )

    assert len(events) == 50


def test_snapshot():

    world = SimulationWorld(
        entity_count=100
    )

    world.generate_events(20)

    snapshot = world.snapshot()

    assert snapshot["entities"] == 100
    assert snapshot["events"] == 20