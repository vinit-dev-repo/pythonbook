class Cart:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Cart({self.items})"

    def __iadd__(self, item):
        self.items.append(item)
        return self

cart = Cart()
cart += "apple"
cart += "bread"
print(cart)
