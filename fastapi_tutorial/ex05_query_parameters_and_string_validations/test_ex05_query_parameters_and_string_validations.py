from fastapi.testclient import TestClient

from fastapi_tutorial.ex05_query_parameters_and_string_validations.main import app

client = TestClient(app)

def test_items_01():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

def test_items_02():
    response = client.get("/items/?q=abc")
    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ],
        "q": "abc"
    }

def test_items_03():
    response = client.get("/items1/?q=abc")
    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ],
        "q": "abc"
    }

def test_items_04():
    q = "a"*60
    response = client.get(f"/items1/?q={q}")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 50},
                'loc': ['query','q'],
                'msg': 'ensure this value has at most 50 characters',
                'type': 'value_error.any_str.max_length'
            }
        ]
    }

def test_items_05():
    q = "a"*2
    response = client.get(f"/items2/?q={q}")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 3},
                'loc': ['query','q'],
                'msg': 'ensure this value has at least 3 characters',
                'type': 'value_error.any_str.min_length'
            }
        ]
    }

def test_items_06():
    response = client.get(f"/items2/?q=abcd")
    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ],
        "q": "abcd"
    }

def test_items_07():
    response = client.get(f"/items3/?q=fixedquery")
    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"}
        ],
        "q": "fixedquery"
    }

def test_items_08():
    response = client.get(f"/items3/?q=wrong")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{'ctx': {'pattern': '^fixedquery$'},
                    'loc': ['query',
                            'q'],
                    'msg': 'string does not match regex "^fixedquery$"',
                    'type': 'value_error.str.regex'}],
    }

def test_items_09():
    response = client.get(f"/items4/")
    assert response.status_code == 200
    assert response.json() == {
        "q": None
    }

def test_items_10():
    response = client.get(f"/items5/")
    assert response.status_code == 200
    assert response.json() == {
        "q": ["foo", "bar"]
    }


def test_items_11():
    response = client.get(f"/items6/?q=abc")
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
        "q": "abc"
    }

def test_items_12():
    response = client.get(f"/items7/")
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
    }

def test_items_13():
    response = client.get(f"/items7/?item-query=abc")
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
         "q": "abc"
    }

def test_items_14():
    response = client.get(f"/items8/")
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
    }

def test_items_15():
    response = client.get(f"/items8/?item-query=fixedquery")
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
         "q": "fixedquery"
    }

def test_items_16():
    response = client.get(f"/items9/?hidden_query=hidden_query")
    assert response.status_code == 200
    assert response.json() == {
         "hidden_query": "hidden_query"
    }

def test_items_17():
    response = client.get(f"/items9/")
    assert response.status_code == 200
    assert response.json() == {
         "hidden_query": "Not found"
    }