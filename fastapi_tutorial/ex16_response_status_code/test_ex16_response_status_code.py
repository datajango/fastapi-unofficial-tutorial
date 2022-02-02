from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex16_response_status_code.main import app

client = TestClient(app)

def test_items():

    name = "callisto"

    response_data = {
        "name": "callisto"
    }

    response = client.post(f"/items/?name={name}")
    assert response.status_code == 201
    assert response.json() == response_data

def test_items1():

    name = "callisto"

    response_data = {
        "name": "callisto"
    }

    response = client.post(f"/items1/?name={name}")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == response_data

