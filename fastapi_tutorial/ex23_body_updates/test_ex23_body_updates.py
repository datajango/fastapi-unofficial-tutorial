from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex23_body_updates.main import app

client = TestClient(app)

def test_get_items():
    item_id = "foo"
    response_data = {'description': None, 'name': 'Foo', 'price': 50.2, 'tags': [], 'tax': 10.5}
    response = client.get(f"/items/{item_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data

def test_put_item():
    item_id = "baz"
    request_data = {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": ["a","b"]}
    response_data = request_data
    response = client.put(f"/items/{item_id}", json=request_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data