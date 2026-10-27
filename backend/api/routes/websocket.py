import asyncio
import random

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()


@router.websocket("/live")
async def live_stream(websocket: WebSocket):
    await websocket.accept()

    print("🔌 Live Monitor connected.")

    try:
        while True:
            event = {
                "type": "live_event",
                "entity_id": f"ENT-{random.randint(1000, 9999)}",
                "event_type": random.choice(
                    [
                        "LOGIN",
                        "TRANSACTION",
                        "MESSAGE",
                        "FILE_ACCESS",
                        "LOCATION_UPDATE",
                        "API_REQUEST",
                    ]
                ),
                "risk_score": round(random.uniform(0.05, 0.99), 3),
                "anomaly": random.random() < 0.15,
            }

            await websocket.send_json(event)

            await asyncio.sleep(2)

    except WebSocketDisconnect:
        print("🔌 Live Monitor disconnected.")

    except asyncio.CancelledError:
        print("🛑 Live Monitor task cancelled.")

    except Exception as exc:
        print(f"⚠️ WebSocket error: {exc}")