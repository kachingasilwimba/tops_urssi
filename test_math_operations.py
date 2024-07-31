from math_opertions import add, subtract, multiply, divide
import pytest

# Test cases
def test_add():
    assert add(1, 2) == 3
    assert add(0, 1) == 1


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 1, 1),
        (2, 3, 5),
        (0, 0, 0),
        (-1, -1, -2),
        (-1, 1, 0),
        (1, -1, 0),
        (1, 0, 1),
        (0, 0, 0),
        (0, 1, 1),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(0, 1) == -1

# @pytest.mark.parametrize("a, b, expected", [(1, 2, -1), (0, 1, -1), (2, 3, -1)])


def test_multiply():
    assert multiply(1, 2) == 2

# @pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (0, 1, 0), (2, 3, 6)])


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(1, 1) == 1

# @pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (0, 1, 0)])
