from fastapi.testclient import TestClient
from fastapi_tutorial.ex14_response_model.main import app, Item

client = TestClient(app)

def test_items_01():

    request_data = {
        "name": "Foo",
        "description": "A awesome item.",
        "price": 15.5,
        "tax": 5.5,
        "tags": ["foo", "bar"]
    }

    response_data = request_data

    response = client.post(f"/items/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_users():

    request_data = {
        "username": "callisto",
        "password": "moon",
        "email": "callisto@jupiter.com",
        "full_name": "Callisto Moon"
    }

    response_data = request_data

    response = client.post(f"/user/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_users_01():

    request_data = {
        "username": "callisto",
        "password": "moon",
        "email": "callisto@jupiter.com",
        "full_name": "Callisto Moon"
    }

    response_data = {
        "username": "callisto",
        "email": "callisto@jupiter.com",
        "full_name": "Callisto Moon"
    }

    response = client.post(f"/user1/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_items_02():

    item_id = "foo"  # must be foo, bar or baz

    response_data = {"name": "Foo", "price": 50.2}

    response = client.get(f"/items2/{item_id}")
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_03():

    item_id = "bar"  # must be foo, bar or baz

    response_data = {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2}

    response = client.get(f"/items2/{item_id}")
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_04():

    item_id = "baz"  # must be foo, bar or baz

    response_data = {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}

    response = client.get(f"/items2/{item_id}")
    assert response.status_code == 200
    assert response.json() == response_data


def test_items_05():

    item_id = "baz"  # must be foo, bar or baz

    response_data = {
        "name": "Baz",
        "description": "There goes my baz",
    }

    response = client.get(f"/items3/{item_id}/name")
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_06():

    item_id = "baz"  # must be foo, bar or baz

    response_data = {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2
    }

    response = client.get(f"/items3/{item_id}/public")
    assert response.status_code == 200
    assert response.json() == response_data