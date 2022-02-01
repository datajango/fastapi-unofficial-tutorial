from fastapi.testclient import TestClient

from fastapi_tutorial.ex08_body_fields.main import app

client = TestClient(app)

def test_items_01():
    item_id = 100
    description = "a" * 301
    price = 0

    request_data = {
        "item": {
            "name": "Foo",
            "description": description,
            "price": price,
            "tax": 7.9
        }
    }

    description_err = {'ctx': {'limit_value': 300},
            'loc': ['body',
                    'item',
                    'description'],
            'msg': 'ensure this value has at most 300 characters',
            'type': 'value_error.any_str.max_length'}

    price_err = {'ctx': {'limit_value': 0},
            'loc': ['body',
                    'item',
                    'price'],
            'msg': 'ensure this value is greater than 0',
            'type': 'value_error.number.not_gt'}

    validation_errors = [description_err, price_err]

    response = client.put(f"/items/{item_id}", json=request_data)
    assert response.status_code == 422
    assert response.json() == {
        "detail": validation_errors
    }
