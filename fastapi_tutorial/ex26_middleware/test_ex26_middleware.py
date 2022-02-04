from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex26_middleware.main import app

client = TestClient(app)

def test_root():
    response_data = {
        "message": "Hello World"
    }
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data
    assert "x-process-time" in response.headers