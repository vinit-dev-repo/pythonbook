class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = Cart()
print(bool(cart))       # no __bool__ defined - Python falls back to __len__
cart.add("apple")
print(bool(cart))
print(len(cart))
