import pytest
from typing import List
from pydantic import BaseModel, ValidationError, conint

def test_error_handling():
    class Location(BaseModel):
        lat = 0.1
        lng = 10.1

    class Model(BaseModel):
        is_required: float
        gt_int: conint(gt=42)
        list_of_ints: List[int] = None
        a_float: float = None
        recursive_model: Location = None

    data = dict(
        list_of_ints=['1', 2, 'bad'],
        a_float='not a float',
        recursive_model={'lat': 4.2, 'lng': 'New York'},
        gt_int=21,
    )

    """
    5 validation errors for Model
        is_required
        field required (type=value_error.missing)
        gt_int
        ensure this value is greater than 42 (type=value_error.number.not_gt; limit_value=42)
        list_of_ints -> 2
        value is not a valid integer (type=type_error.integer)
        a_float
        value is not a valid float (type=type_error.float)
        recursive_model -> lng
        value is not a valid float (type=type_error.float)
    """

    with pytest.raises(ValidationError) as exc_info:
        mdl = Model(**data)

    #for index, error in enumerate(exc_info.value.errors()):
    #    print(index, error)
    assert len(exc_info.value.errors()) == 5

    # {'loc': ('is_required',), 'msg': 'field required', 'type': 'value_error.missing'}
    # {'loc': ('gt_int',), 'msg': 'ensure this value is greater than 42', 'type': 'value_error.number.not_gt', 'ctx': {'limit_value': 42}}
    # {'loc': ('list_of_ints', 2), 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}
    # {'loc': ('a_float',), 'msg': 'value is not a valid float', 'type': 'type_error.float'}
    # {'loc': ('recursive_model', 'lng'), 'msg': 'value is not a valid float', 'type': 'type_error.float'}

    try:
        Model(**data)
    except ValidationError as e:
        assert len(e.errors()) == 5

        #print(e.json())
        """
        [
        {
            "loc": [
            "is_required"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
            "gt_int"
            ],
            "msg": "ensure this value is greater than 42",
            "type": "value_error.number.not_gt",
            "ctx": {
            "limit_value": 42
            }
        },
        {
            "loc": [
            "list_of_ints",
            2
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        },
        {
            "loc": [
            "a_float"
            ],
            "msg": "value is not a valid float",
            "type": "type_error.float"
        },
        {
            "loc": [
            "recursive_model",
            "lng"
            ],
            "msg": "value is not a valid float",
            "type": "type_error.float"
        }
        ]
        """