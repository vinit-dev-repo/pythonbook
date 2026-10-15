# test_exceptions.py
import pytest
from calculator import divide

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
