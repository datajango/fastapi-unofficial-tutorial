from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex17_form_data.main import app

client = TestClient(app)

def test_login():
    form_data  = {
        "username": "callisto",
        "password": "moon"
    }

    response_data = {
        "username": "callisto"
    }

    response = client.post(f"/login/", data=form_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data