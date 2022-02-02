from fastapi.testclient import TestClient
from fastapi_tutorial.ex15_extra_models.main import app

client = TestClient(app)

def test_user():

    request_data = {
        "username": "callisto",
        "password": "jupiter123",
        "email": "callosto@jupiter.com",
        "full_name": "Callisto Moon"
    }

    response_data =  {
        "username": "callisto",
        "email": "callosto@jupiter.com",
        "full_name": "Callisto Moon"
    }

    response = client.post(f"/user/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data
