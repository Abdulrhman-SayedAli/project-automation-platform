from fastapi.testclient import TestClient

from app.main import create_app


def test_health_endpoint_returns_api_status() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["success"] is True
    assert payload["status"] == "ok"
    assert payload["components"]["api"]["status"] == "ok"


def test_openapi_schema_renders() -> None:
    client = TestClient(create_app())

    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "AI Software Factory"

