from fastapi.testclient import TestClient

from fastapi_tutorial.ex06_path_parameters_and_numeric_validations.main import app

client = TestClient(app)

def test_items_01():
    response = client.get("/items/100")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 100
    }

def test_items_02():
    response = client.get("/items/100/?item-query=filter")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 100,
        "q": "filter"
    }

def test_items_03():
    response = client.get("/items1/0")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 1},
                'loc': ['path', 'item_id'],
                'msg': 'ensure this value is greater than or equal to 1',
                'type': 'value_error.number.not_ge'
            }
        ],
    }

def test_items_04():
    response = client.get("/items1/1001")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 1000},
                'loc': ['path', 'item_id'],
                'msg': 'ensure this value is less than or equal to 1000',
                'type': 'value_error.number.not_le'
            }
        ],
    }

def test_items_05():
    response = client.get("/items2/50?size=5.32")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 50,
        "size": 5.32
    }

def test_items_06():
    response = client.get("/items2/50?size=55.32")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 10.5},
                'loc': ['query', 'size'],
                'msg': 'ensure this value is less than 10.5',
                'type': 'value_error.number.not_lt'
            }
        ],
    }

