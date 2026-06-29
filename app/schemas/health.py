from pydantic import BaseModel, Field


class ComponentHealth(BaseModel):
    status: str
    detail: str | None = None


class HealthResponse(BaseModel):
    success: bool = True
    status: str = "ok"
    service: str
    version: str
    environment: str
    components: dict[str, ComponentHealth] = Field(default_factory=dict)

