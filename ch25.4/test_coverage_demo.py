# test_coverage_demo.py
from calculator import add, divide

def test_addition_result():
    assert add(2, 3) == 5

def test_division_result():
    assert divide(10, 2) == 5
