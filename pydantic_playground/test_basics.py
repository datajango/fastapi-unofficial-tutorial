# Learn Pydantic by writing Unit Tests
# By Anthony Leotta
import pytest
from pydantic import BaseModel, error_wrappers
from datetime import datetime
from typing import List, Optional


def test_pass_parameters():

    class User(BaseModel):
        id: int
        name = 'Jane Doe'

    user = User(id=123)

    assert user.id == 123
    assert user.name == 'Jane Doe'
    assert user.__fields_set__ == {'id'}
    assert user.dict() == dict(user) == {'id': 123, 'name': 'Jane Doe'}

def test_validation_error():

    class User(BaseModel):
        id: int
        name = 'Jane Doe'

    # User requires an id
    with pytest.raises(error_wrappers.ValidationError):
        user = User()

def test_var_args():
    class User(BaseModel):
        id: int
        name = 'John Doe'
        signup_ts: Optional[datetime] = None
        friends: List[int] = []

    external_data = {
        'id': '123',
        'signup_ts': '2019-06-01 12:22',
        'friends': [1, 2, '3'],
    }

    # pass in **kwargs is a common idiom to allow arbitrary number of arguments to
    user = User(**external_data)



