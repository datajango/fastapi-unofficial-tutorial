from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex20_handling_errors.main import app

client = TestClient(app)

def test_items():

    item_id = "err"

    response_data = {
        "detail": "Item not found"
    }

    response = client.get(f"/items/{item_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == response_data
    assert response.headers.get("x-error") == "There goes my error"

def test_unicorns():

    name = "yolo"

    response_data = {
        "message": "Oops! yolo did something. There goes a rainbow..."
    }

    response = client.get(f"/unicorns/{name}")

    assert response.status_code == 418
    assert response.json() == response_data
