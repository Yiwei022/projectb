from src.utils import add, sub


def test_add():
    assert 0 == add(-1, 1)
    assert 6 == add(1, 2, 3)


def test_sub():
    assert 0 == sub(1, 1)
    assert -4 == sub(1, 2, 3)
