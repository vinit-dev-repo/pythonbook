# test_practice.py
# 1
def is_even(n):
    return n % 2 == 0

def test_is_even_happy_path():
    assert is_even(4) is True

def test_is_even_zero():
    assert is_even(0) is True

def test_is_even_odd():
    assert is_even(7) is False


# 2
def safe_sqrt(n):
    if n < 0:
        raise ValueError("cannot take the square root of a negative number")
    return n ** 0.5

import pytest

def test_safe_sqrt_happy_path():
    assert safe_sqrt(9) == 3

def test_safe_sqrt_negative_raises():
    with pytest.raises(ValueError):
        safe_sqrt(-4)


# 3
@pytest.mark.parametrize("n, expected", [
    (4, True),
    (0, True),
    (7, False),
    (-2, True),
])
def test_is_even_many_cases(n, expected):
    assert is_even(n) is expected


# 4
import unittest

class TestSafeSqrt(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(safe_sqrt(9), 3)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            safe_sqrt(-4)
