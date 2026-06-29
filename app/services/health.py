from app.core.config import Settings
from app.core.logging import get_logger
from app.schemas.health import ComponentHealth, HealthResponse


class HealthService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._logger = get_logger(__name__)

    async def check(self) -> HealthResponse:
        self._logger.info("health_check_requested", event_type="health_check")
        return HealthResponse(
            service=self._settings.app_name,
            version=self._settings.app_version,
            environment=self._settings.environment,
            components={
                "api": ComponentHealth(status="ok"),
            },
        )

