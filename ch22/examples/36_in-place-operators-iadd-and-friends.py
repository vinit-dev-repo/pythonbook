class BrokenCart:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"BrokenCart({self.items})"

    def __iadd__(self, item):
        self.items.append(item)
        # BUG: forgot "return self"

cart = BrokenCart()
cart += "apple"
print(cart)
