import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TypedDict

from fastapi import FastAPI

from app.core.config import ConfigSummary, settings
from app.templates.router import router as templates_router


class HealthStatus(TypedDict):
    status: str
    env: str
    version: str
    config: ConfigSummary


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan function to perform startup and shutdown tasks.
    """
    # Perform startup tasks here (e.g., connect to databases, initialize resources)
    print("Starting up NotifyHQ...")
    print("Configuration Summary:", settings.summary())
    yield
    # Perform shutdown tasks here (e.g., close database connections, clean up resources)
    print("Shutting down NotifyHQ...")


app = FastAPI(
    title="NotifyHQ",
    version=settings.app_version,
    description="NotifyHQ is a notification service that allows you to send notifications to various channels such as email, SMS, and push notifications.",
    docs_url=None if settings.app_env == "production" else "/docs",
    redoc_url=None if settings.app_env == "production" else "/redoc",
    lifespan=lifespan,
)
# Routers
app.include_router(templates_router, prefix=settings.api_v1_prefix)


# Routes
@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint to verify that the application is running.
    """
    return {"status": "ok", "env": settings.app_env}


@app.get("/health/detailed", tags=["Health"])
async def health_detailed() -> HealthStatus:
    """
    Detailed health check endpoint to verify the status of various components.
    """
    # Here you can add checks for database connectivity, message broker status, etc.
    await asyncio.sleep(0)  # Simulate some checks
    return {
        "status": "ok",
        "env": settings.app_env,
        "version": settings.app_version,
        "config": settings.summary(),
    }
