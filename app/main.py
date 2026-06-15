from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title="NotifyHQ",
    version="1.0.0",
    description="NotifyHQ is a notification service that allows you to send notifications to various channels such as email, SMS, and push notifications.",
    docs_url=None if settings.app_env == "production" else "/docs",
    redoc_url=None if settings.app_env == "production" else "/redoc",
)


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint to verify that the application is running.
    """
    return {"status": "ok", "env": settings.app_env}
