# test_multiples.py
from multiples import is_multiple_of_three

def test_three_is_a_multiple_of_three():
    assert is_multiple_of_three(3) is True

def test_four_is_not_a_multiple_of_three():
    assert is_multiple_of_three(4) is False
