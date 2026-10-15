# test_average.py
import pytest
from calculator import average

def test_average_happy_path():
    assert average([2, 4, 6]) == 4

def test_average_single_number():          # edge case
    assert average([5]) == 5

def test_average_negative_numbers():        # edge case
    assert average([-2, 2]) == 0

def test_average_empty_list_raises():       # error case
    with pytest.raises(ValueError):
        average([])
