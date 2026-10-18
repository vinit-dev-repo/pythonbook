@pytest.fixture
def cart_with_cherry(shopping_cart):
    shopping_cart.append("cherry")
    return shopping_cart

def test_dependencies_share_one_cart(shopping_cart, cart_with_cherry):
    assert shopping_cart is cart_with_cherry
    assert shopping_cart == ["apple", "banana", "cherry"]

def test_another_test_starts_fresh(shopping_cart):
    assert shopping_cart == ["apple", "banana"]
