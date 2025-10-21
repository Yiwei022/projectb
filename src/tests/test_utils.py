import pytest
from src.features import mul, div
from src.utils import add, sub


def test_add():
    assert 0 == add(-1, 1)
    assert 6 == add(1, 2, 3)


def test_sub():
    assert 0 == sub(1, 1)
    assert -4 == sub(1, 2, 3)


def test_mul_integers():
    assert mul(3, 4) == 12


def test_mul_floats():
    assert mul(2.5, 4.0) == 10.0


def test_mul_zero():
    assert mul(0, 100) == 0


def test_div_integers():
    assert div(10, 2) == 5


def test_div_floats():
    assert div(9.0, 3.0) == 3.0


def test_div_negative():
    assert div(-10, 2) == -5


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
