from fastapi.testclient import TestClient

from fastapi_tutorial.ex09_body_nested_models.main import app
from unittest import TestCase

client = TestClient(app)


def test_items_01():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["a", "b", "c"]
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2,
            "tags": ["a", "b", "c"]
        }
    }

    response = client.put(f"/items/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_items_02():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 42.0,
        "tax": 3.2,
        "tags": [1.0, 2, 3, "a"]
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2,
            "tags": ["1.0", "2", "3", "a"]
        }
    }

    response = client.put(f"/items/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_items_03():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["a", "a", "b", "c"]
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2,
            "tags": ["a", "a", "b", "c"]
        }
    }

    response = client.put(f"/items2/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_items_04():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["a"],
        "image": {
            "url": "https://test.com/ld93mdn2d2.jpg",
            "name": "image42"
        }
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2,
            "tags": ["a"],
            "image": {
                "url": "https://test.com/ld93mdn2d2.jpg",
                "name": "image42"
            }
        }
    }

    response = client.put(f"/items3/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_05():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": [
            "rock",
            "metal",
            "bar"
        ],
        "images": [
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2,
            "tags": [
                "rock",
                "metal",
                "bar"
            ],
            "images": [
                {
                    "url": "http://example.com/baz.jpg",
                    "name": "The Foo live"
                },
                {
                    "url": "http://example.com/dave.jpg",
                    "name": "The Baz"
                }
            ]
        }
    }

    response = client.put(f"/items4/{item_id}", json=request_data)
    assert response.status_code == 200

    # this fails because sets are unordered, this is a bug in Python assert ==
    assert response.json() == response_data
    #TestCase().assertDictEqual(response_data, response.json())



def test_items_04():

    item_id = 100

    request_data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["a"],
        "image": {
            "url": "https://test.com/ld93mdn2d2.jpg",
            "name": "image42"
        }
    }

    response_data = {
        "item_id": item_id,
        "item": {
            "name": "Foo",
            "description": "An optional description",
            "price": 42.0,
            "tax": 3.2,
            "tags": ["a"],
            "image": {
                "url": "https://test.com/ld93mdn2d2.jpg",
                "name": "image42"
            }
        }
    }

    response = client.put(f"/items3/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_offers():

    request_data = {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "items": [
            {
                "name": "Foo",
                "description": "The pretender",
                "price": 42.0,
                "tax": 3.2,
                "tags": [
                    "rock",
                    "metal",
                    "bar"
                ],
                "images": [
                    {
                        "url": "http://example.com/baz.jpg",
                        "name": "The Foo live"
                    },
                    {
                        "url": "http://example.com/dave.jpg",
                        "name": "The Baz"
                    }
                ]
            },
             {
                "name": "Foo",
                "description": "The pretender",
                "price": 42.0,
                "tax": 3.2,
                "tags": [
                    "rock",
                    "metal",
                    "bar"
                ],
                "images": [
                    {
                        "url": "http://example.com/baz.jpg",
                        "name": "The Foo live"
                    },
                    {
                        "url": "http://example.com/dave.jpg",
                        "name": "The Baz"
                    }
                ]
            },
             {
                "name": "Foo",
                "description": "The pretender",
                "price": 42.0,
                "tax": 3.2,
                "tags": [
                    "rock",
                    "metal",
                    "bar"
                ],
                "images": [
                    {
                        "url": "http://example.com/baz.jpg",
                        "name": "The Foo live"
                    },
                    {
                        "url": "http://example.com/dave.jpg",
                        "name": "The Baz"
                    }
                ]
            }
        ]
    }

    response_data = request_data

    response = client.post(f"/offers/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_images_multiple():

    request_data = [
        {
            "url": "https://www.test.com/1.jpg",
            "name": "1"
        },
        {
            "url": "https://www.test.com/2.jpg",
            "name": "2"
        },
        {
            "url": "https://www.test.com/3.jpg",
            "name": "3"
        },
        {
            "url": "https://www.test.com/4.jpg",
            "name": "4"
        },
        {
            "url": "https://www.test.com/5.jpg",
            "name": "5"
        }
    ]

    response_data = request_data

    response = client.post(f"/images/multiple/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data

def test_index_weights():

    request_data = {
        "1": 1.0,
        "2": 5.6,
        "3": 7.4,
    }

    response_data = request_data

    response = client.post("/index-weights/", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data
