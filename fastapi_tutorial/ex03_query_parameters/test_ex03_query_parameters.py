from fastapi.testclient import TestClient

from fastapi_tutorial.ex03_query_parameters.main import app, fake_items_db

client = TestClient(app)

def test_items_01():
    response = client.get("/items?skip=0&limit=10")
    assert response.status_code == 200
    assert response.json() == fake_items_db[0:10]

def test_items_02():
    response = client.get("/items?skip=0&limit=1")
    assert response.status_code == 200
    assert response.json() == fake_items_db[0:1]

def test_items_03():
    response = client.get("/items?skip=1&limit=1")
    assert response.status_code == 200
    assert response.json() == fake_items_db[1:2]

def test_items_04():
    response = client.get("/items/abc")
    assert response.status_code == 200
    assert response.json() == {
        "description": "This is an amazing item that has a long description",
        "item_id": "abc",
    }

def test_items_05():
    response = client.get("/items/abc?skip=0&limit=10&q=abc")
    assert response.status_code == 200
    assert response.json() == {
        "q": "abc",
        "description": "This is an amazing item that has a long description",
        "item_id": "abc",
    }

def test_items_06():
    response = client.get("/items/abc?skip=0&limit=10&q=abc")
    assert response.status_code == 200
    assert response.json() == {
        "description": "This is an amazing item that has a long description",
        "q": "abc",
        "item_id": "abc",
    }


def test_items_07():
    response = client.get("/items/abc?skip=0&limit=10&q=abc&short=True")
    assert response.status_code == 200
    assert response.json() == {
        "description": "Amazing",
        "q": "abc",
        "item_id": "abc",
    }

def test_items_08():
    response = client.get("/items/abc?skip=0&limit=10&short=True")
    assert response.status_code == 200
    assert response.json() == {
        "description": "Amazing",
        "item_id": "abc",
    }

def test_users_01():
    response = client.get("/users/123/items/abc?q=ABC")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": "abc",
        "owner_id": 123,
        "description": "This is an amazing item that has a long description",
        "q": "ABC"
    }

def test_items2():
    response = client.get("/items2/abc?needy=T")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": "abc",
        "needy": "T",
        "skip": 0,
        "limit": None
    }