from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex20_handling_errors.main_plain_exception import app

client = TestClient(app)

def test_items():

    item_id = "foo"

    validation_error_str_lines = [
        b"1 validation error for Request",
        b"path -> item_id",
        b"  value is not a valid integer (type=type_error.integer)",
    ]

    response = client.get(f"/items/{item_id}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.content == b"\n".join(validation_error_str_lines)