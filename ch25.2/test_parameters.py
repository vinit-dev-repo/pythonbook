# test_parameters.py
import pytest
from calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300),
    (-5, 5, 0),
])
def test_add_many_cases(a, b, expected):
    assert add(a, b) == expected
