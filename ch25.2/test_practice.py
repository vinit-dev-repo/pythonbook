# test_practice.py
import pytest

def safe_sqrt(n):
    if n < 0:
        raise ValueError("cannot take the square root of a negative number")
    return n ** 0.5

def is_even(n):
    return n % 2 == 0

# 1
def test_safe_sqrt_happy_path():
    assert safe_sqrt(9) == 3

def test_safe_sqrt_negative_raises():
    with pytest.raises(ValueError):
        safe_sqrt(-4)

# 2
@pytest.mark.parametrize("n, expected", [(4, True), (0, True), (7, False), (-2, True)])
def test_is_even_many_cases(n, expected):
    assert is_even(n) is expected

# 3
@pytest.fixture
def empty_list():
    return []

def test_append_changes_only_this_test(empty_list):
    empty_list.append("x")
    assert empty_list == ["x"]

def test_next_test_starts_empty(empty_list):
    assert empty_list == []

# 4
class Counter:
    def __init__(self):
        self.value = 0

    def add(self, n):
        if n < 0:
            raise ValueError("n must not be negative")
        self.value += n

def test_rejected_add_keeps_value():
    counter = Counter()
    counter.add(2)
    with pytest.raises(ValueError):
        counter.add(-1)
    assert counter.value == 2
