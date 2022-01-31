from fastapi.testclient import TestClient

from fastapi_tutorial.ex01_first_steps.main import app

client = TestClient(app)

def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "method": 'GET', "message": "Hello World"}

def test_post_main():
    response = client.post(
        "/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == { "method": 'POST', "request": {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}}

def test_patch_main():
    response = client.patch(
        "/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == { "method": 'PATCH', "request": {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}}

def test_put_main():
    response = client.put(
        "/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == { "method": 'PUT', "request": {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}}

def test_delete_main():
    response = client.delete(
        "/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == { "method": 'DELETE', "request": {"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}}

def test_options_main():
    response = client.options("/")
    assert response.status_code == 200
    assert response.json() == { "method": 'OPTIONS' }

def test_head_main():
    response = client.head("/")
    assert response.status_code == 200

def test_trace_main():
    response = client.head("/")
    assert response.status_code == 200

