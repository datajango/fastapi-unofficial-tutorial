from fastapi.testclient import TestClient
from fastapi_tutorial.ex27_cors.main import app


def test_negative_cors():

    client = TestClient(app)

    # Test pre-flight response negative case
    # the origin is not allowed

    headers = {
        "Origin": "https://localhost.notallowed.com",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "X-Example",
    }
    response = client.options("/", headers=headers)
    assert response.status_code == 400
    assert response.text == "Disallowed CORS origin"
    assert "access-control-allow-origin" not in response.headers


def test_cors():
    client = TestClient(app)
    # Test pre-flight response
    headers = {
        "Origin": "https://localhost.tiangolo.com",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "X-Example",
    }
    response = client.options("/", headers=headers)
    assert response.status_code == 200, response.text
    assert response.text == "OK"
    assert (
        response.headers["access-control-allow-origin"]
        == "https://localhost.tiangolo.com"
    )
    assert response.headers["access-control-allow-headers"] == "X-Example"

    # Test standard response
    headers = {"Origin": "https://localhost.tiangolo.com"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World"}
    assert (
        response.headers["access-control-allow-origin"]
        == "https://localhost.tiangolo.com"
    )

    # Test non-CORS response
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello World"}
    assert "access-control-allow-origin" not in response.headers