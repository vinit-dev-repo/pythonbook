import unittest

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ["apple", "banana"]     # fresh cart before EVERY test

    def test_starts_with_two_items(self):
        self.assertEqual(len(self.cart), 2)

    def test_can_add_item(self):
        self.cart.append("cherry")
        self.assertEqual(self.cart, ["apple", "banana", "cherry"])
