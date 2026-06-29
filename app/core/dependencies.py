from app.core.config import Settings, get_settings
from app.services.health import HealthService


def get_health_service() -> HealthService:
    return HealthService(settings=get_settings())


def get_app_settings() -> Settings:
    return get_settings()

