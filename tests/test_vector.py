from src.vector import Vector
from src.body import Body
import pytest

def test_vector_addition():
    v1 = Vector(1, 2)
    v2 = Vector(4, 5)
    result = v1 + v2
    assert result.x == 5 and result.y == 7

def test_vector_subtraction():
    v1 = Vector(10, 5)
    v2 = Vector(2, 1)
    result = v1 - v2
    assert result.x == 8 and result.y == 4

def test_vector_scalar_multiplication():
    v = Vector(1, -2)
    result = v * 3
    assert result.x == 3 and result.y == -6

def test_vector_magnitude():
    v = Vector(3, 4)
    assert pytest.approx(v.mag(), 0.001) == 5.0

def test_vector_repr():
    v = Vector(3, 4)
    assert repr(v) == "Vector(3.0, 4.0)"
