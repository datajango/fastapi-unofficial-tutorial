import pytest
from typing import List
from pydantic import BaseModel, ValidationError, validator

def text_custom_validators():
    class Model(BaseModel):
        foo: str

        @validator('foo')
        def value_must_equal_bar(cls, v):
            if v != 'bar':
                raise ValueError('value must be "bar"')

            return v

    try:
        Model(foo='ber')
    except ValidationError as e:
        print(e.errors())

        assert len(e.errors()) == 1

        """
        [
            {
                'loc': ('foo',),
                'msg': 'value must be "bar"',
                'type': 'value_error',
            },
        ]
        """