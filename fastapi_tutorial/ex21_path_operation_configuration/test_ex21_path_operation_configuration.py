from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex21_path_operation_configuration.main import app
from typing import Optional, Set

client = TestClient(app)

def test_items():

    request_data = {
        "name": "foo",
        "description": "foobar",
        "price": 1.0,
        "tax": 0.01,
        "tags": ["a", "b"]
    }

    response_data = {
        "name": "foo",
        "description": "foobar",
        "price": 1.0,
        "tax": 0.01,
        "tags": ["a", "b"]
    }

    response = client.post(f"/items/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == response_data


def test_items1():

    request_data = {
        "name": "foo",
        "description": "foobar",
        "price": 1.0,
        "tax": 0.01,
        "tags": ["a", "b"]
    }

    response_data = {
        "name": "foo",
        "description": "foobar",
        "price": 1.0,
        "tax": 0.01,
        "tags": ["a", "b"]
    }

    response = client.post(f"/items/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == response_data