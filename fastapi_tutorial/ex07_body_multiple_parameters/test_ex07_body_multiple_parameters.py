from fastapi.testclient import TestClient

from fastapi_tutorial.ex07_body_multiple_parameters.main import app

client = TestClient(app)

def test_items_01():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 42.0,
        "tax": 3.2
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        }
    }

    response = client.put(f"/items/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_02():

    item_id = 100

    request_data = {
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "apple123",
            "full_name": "Johnny Appleseed"
        }
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "apple123",
            "full_name": "Johnny Appleseed"
        }
    }

    response = client.put(f"/items1/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_03():

    item_id = 100

    request_data = {
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "apple123",
            "full_name": "Johnny Appleseed"
        },
        "importance": 1
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "apple123",
            "full_name": "Johnny Appleseed"
        },
        "importance": 1
    }

    response = client.put(f"/items2/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_04():

    item_id = 100

    request_data = {
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "apple123",
            "full_name": "Johnny Appleseed"
        },
        "importance": 1
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "apple123",
            "full_name": "Johnny Appleseed"
        },
        "importance": 1,
        "q": "foo"
    }

    response = client.put(f"/items3/{item_id}?q=foo", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_items_05():

    item_id = 100

    request_data = {
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        }
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2
        }
    }

    response = client.put(f"/items4/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data
