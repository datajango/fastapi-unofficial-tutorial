from fastapi.testclient import TestClient
from fastapi_tutorial.ex12_cookie_parameters.main import app

client = TestClient(app)

def test_items_01():
    cookies = {"ads_id": "foo"}

    response_data = {
        "ads_id": "foo",
    }

    response = client.get(f"/items/", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == response_data