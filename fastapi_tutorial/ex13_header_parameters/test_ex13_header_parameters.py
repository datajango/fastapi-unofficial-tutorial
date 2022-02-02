from fastapi.testclient import TestClient
from fastapi_tutorial.ex13_header_parameters.main import app

client = TestClient(app)

def test_items_01():
    headers = {"User-Agent": "foo"}

    response_data = {
        "User-Agent": "foo",
    }

    response = client.get(f"/items/", headers=headers)
    assert response.status_code == 200
    assert response.json() == response_data

def test_items_02():
    headers = {"strange_header": "foo"}

    response_data = {
        "strange_header": "foo",
    }

    response = client.get(f"/items1/", headers=headers)
    assert response.status_code == 200
    assert response.json() == response_data

# def test_items_03():
#     headers = [
#         "X-Token: foo",
#         "X-Token: bar"
#     ]

#     response_data = {
#         "X-Token values": ["foo","bar"]
#     }

#     response = client.get(f"/items2/", headers=headers)
#     assert response.status_code == 200
#     assert response.json() == response_data