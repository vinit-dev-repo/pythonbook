STARTING_ITEMS = ("apple", "banana")

@pytest.fixture
def shopping_cart():
    return list(STARTING_ITEMS)
