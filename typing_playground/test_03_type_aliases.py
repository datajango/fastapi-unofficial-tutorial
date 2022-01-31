import inspect

def test_type_aliases():
    Vector = list[float]

    def scale(scalar: float, vector: Vector) -> Vector:
        return [scalar * num for num in vector]

    # typechecks; a list of floats qualifies as a Vector.
    new_vector = scale(2.0, [1.0, -4.2, 5.4])

    assert new_vector == [2.0, -8.4, 10.80]

    signature = inspect.signature(scale)
    assert signature.return_annotation == Vector
    assert len(signature.parameters) == 2
    assert 'scalar' in signature.parameters
    assert 'vector' in signature.parameters
    assert signature.parameters['scalar'].annotation == float
    assert signature.parameters['vector'].annotation == Vector

def test_simplifying_complex_type_signatures():
    from collections.abc import Sequence

    ConnectionOptions = dict[str, str]
    Address = tuple[str, int]
    Server = tuple[Address, ConnectionOptions]

    def broadcast_message(message: str, servers: Sequence[Server]) -> None:
        pass

    signature = inspect.signature(broadcast_message)
    assert signature.return_annotation == None
    assert len(signature.parameters) == 2
    assert 'message' in signature.parameters
    assert 'servers' in signature.parameters
    assert signature.parameters['message'].annotation == str
    assert signature.parameters['servers'].annotation == Sequence[tuple[tuple[str, int], dict[str, str]]]