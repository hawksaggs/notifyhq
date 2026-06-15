from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings


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
    version="1.0.0",
    description="NotifyHQ is a notification service that allows you to send notifications to various channels such as email, SMS, and push notifications.",
    docs_url=None if settings.app_env == "production" else "/docs",
    redoc_url=None if settings.app_env == "production" else "/redoc",
    lifespan=lifespan,
)


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint to verify that the application is running.
    """
    return {"status": "ok", "env": settings.app_env}
