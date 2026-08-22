from datetime import datetime, timezone
from fastapi import APIRouter
from app.core.config import settings
from app.schemas.portfolio import SystemHealth

router = APIRouter(prefix="/sys", tags=["System & Infrastructure"])


@router.get("/health", response_model=SystemHealth)
async def get_health_status() -> SystemHealth:
    """
    Endpoint to check the health status of the application.
    Returns a JSON response with the current operational status, environment, timestamp, and infrastructure provider.
    """
    return SystemHealth(
        status="Online",
        environment=settings.ENVIRONMENT,
        timestamp=datetime.now(timezone.utc),
        hosted_on="Google Cloud Run",
        message="All backend microserviceces operational.",
    )
