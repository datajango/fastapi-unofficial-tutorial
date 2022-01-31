from fastapi.testclient import TestClient

from fastapi_tutorial.ex02_path_parameters.main import app

client = TestClient(app)

def test_get_users_me():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "the current user"}

def test_users():
    response = client.get("/users/tiberius")
    assert response.status_code == 200
    assert response.json() == {"user_id": "tiberius"}

def test_items():
    response = client.get("/items/1701")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1701}

def test_colors_01():
    response = client.get("/colors/Red")
    assert response.status_code == 200
    assert response.json() == {"color_name": "Red", "message": "Red is a nice color."}

def test_colors_02():
    response = client.get("/colors/Blue")
    assert response.status_code == 200
    assert response.json() == {"color_name": "Blue", "message": "Blue is the color of the sky."}

def test_colors_03():
    response = client.get("/colors/Green")
    assert response.status_code == 200
    assert response.json() == {"color_name": "Green",  "message": "Green is the color of grass."}

def test_files():
    response = client.get("/files//home")
    assert response.status_code == 200
    assert response.json() == {"file_path": "/home"}