# test_calculator.py
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_divide():
    assert divide(10, 2) == 5
