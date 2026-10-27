from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import settings
from backend.core.logging import configure_logging

from backend.database.database import (
    Base,
    engine,
)

from backend.api.routes import (
    dashboard,
    entities,
    anomalies,
    simulation,
    graph,
    analytics,
    websocket,
)


configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(
        bind=engine
    )

    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Adaptive Graph Intelligence "
        "& Anomaly Detection System"
    ),
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    dashboard.router,
    prefix="/api/dashboard",
)

app.include_router(
    entities.router,
    prefix="/api/entities",
)

app.include_router(
    anomalies.router,
    prefix="/api/anomalies",
)

app.include_router(
    simulation.router,
    prefix="/api/simulation",
)

app.include_router(
    graph.router,
    prefix="/api/graph",
)

app.include_router(
    analytics.router,
    prefix="/api/analytics",
)

app.include_router(
    websocket.router,
    prefix="/api",
)


@app.get("/health")
def health():

    return {
        "status": "online",
        "system": "ARGUS",
        "version": settings.app_version,
    }