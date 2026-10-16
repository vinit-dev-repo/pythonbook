import pytest

@pytest.fixture
def shopping_cart():
    return ["apple", "banana"]

def test_cart_starts_with_two_items(shopping_cart):
    assert len(shopping_cart) == 2

def test_cart_can_add_item(shopping_cart):
    shopping_cart.append("cherry")
    assert shopping_cart == ["apple", "banana", "cherry"]
