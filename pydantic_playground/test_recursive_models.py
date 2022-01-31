# Learn Pydantic by writing Unit Tests
# By Anthony Leotta
import pytest
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, error_wrappers


class Foo(BaseModel):
    count: int
    size: float = None


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]

def test_recursive_models():
    m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    assert len(m.bars)==2
    """
    {
        'foo': {'count': 4, 'size': None},
        'bars': [
            {'apple': 'x1', 'banana': 'y'},
            {'apple': 'x2', 'banana': 'y'},
        ],
    }
    """