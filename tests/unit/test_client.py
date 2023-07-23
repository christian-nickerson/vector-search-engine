from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health() -> None:
    """test health endpoint returns correctly"""
    response = client.get("/health")
    assert response.status_code == 200
