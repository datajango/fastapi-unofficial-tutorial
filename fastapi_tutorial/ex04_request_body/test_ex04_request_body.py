from fastapi.testclient import TestClient

from fastapi_tutorial.ex04_request_body.main import app

client = TestClient(app)

def test_items_01():
    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }

    response_data = {
        "id": 1,
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5,
        "price_with_tax": 45.2 + 3.5
    }

    response = client.post("/items/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_02():
    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }

    response_data = {
        "id": 100,
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5,
        "price_with_tax": 45.2 + 3.5,
        "q" : "foo"
    }

    response = client.post("/items/100?q=foo", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data
