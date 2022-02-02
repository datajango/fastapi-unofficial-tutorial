from fastapi.testclient import TestClient
from fastapi_tutorial.ex15_extra_models.main_union import app

client = TestClient(app)

def test_get_one_item():

    item_id = "item2"


    response_data =  {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    }

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == response_data


def test_items():

    response_data = [
        {"name": "Foo", "description": "There comes my hero"},
        {"name": "Red", "description": "It's my aeroplane"},
    ]

    response = client.get(f"/items/")
    assert response.status_code == 200
    assert response.json() == response_data


def test_keyword_weights():

    response_data = {"foo": 2.3, "bar": 3.4}

    response = client.get(f"/keyword-weights/")
    assert response.status_code == 200
    assert response.json() == response_data
