# test_even.py
def is_even(n):
    return n % 2 == 0

def test_is_even_happy_path():
    assert is_even(4) is True

def test_is_even_zero():
    assert is_even(0) is True

def test_is_even_odd():
    assert is_even(7) is False
