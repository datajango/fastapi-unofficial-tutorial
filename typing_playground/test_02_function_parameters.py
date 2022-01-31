import inspect
from typing import List

def test_parameters():
    def greeting(name: str) -> str:
        return 'Hello ' + name

    signature = inspect.signature(greeting)
    assert signature.return_annotation == str
    assert len(signature.parameters) == 1
    assert 'name' in signature.parameters
    assert signature.parameters['name'].annotation != int
    assert signature.parameters['name'].annotation == str



