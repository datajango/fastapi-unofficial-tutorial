import inspect
from typing import List

def test_str_signature():
    def greeting(name: str) -> str:
        return 'Hello ' + name

    signature = inspect.signature(greeting)
    assert signature.return_annotation != int
    assert signature.return_annotation == str

def test_int_signature():
    def greeting(name: str) -> int:
        return 42

    signature = inspect.signature(greeting)
    assert signature.return_annotation == int

def test_list_signature():
    def greeting(name: str) -> List:
        return [1,2,3]

    signature = inspect.signature(greeting)
    assert signature.return_annotation == List


def test_list_of_int_signature():
    def greeting(name: str) -> List[int]:
        return [1,2,3]

    signature = inspect.signature(greeting)
    assert signature.return_annotation == List[int]


def test_list_of_str_signature():
    def greeting(name: str) -> List[str]:
        return [1,2,3]

    signature = inspect.signature(greeting)
    assert signature.return_annotation == List[str]