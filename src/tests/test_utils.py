import pytest

from src.features import multiplying,dividing

def test_multiplying_integers():
    assert multiplying(3,4) == 12

def test_multiplying_floats():
    assert multiplying(2.5,4.0) == 10.0

def test_multiplying_zero():
    assert multiplying(0, 100) == 0

def test_dividing_integers():
    assert dividing(10,2) == 5

def test_dividing_floats():
    assert dividing(9.0,3.0) == 3.0

def test_dividing_negative():
    assert dividing(-10, 2) == -5

def test_dividing_by_zero():
    with pytest.raises(ZeroDivisionError):
        dividing(5, 0)