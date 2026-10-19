class InventoryError(Exception):
    """Base class for expected inventory failures."""
    pass

class OutOfStockError(InventoryError):
    def __init__(self, item, requested, available):
        super().__init__(f"Only {available} of {item!r} left, requested {requested}")
        self.item = item
        self.requested = requested
        self.available = available

class UnknownItemError(InventoryError):
    def __init__(self, item):
        super().__init__(f"No such item: {item!r}")
        self.item = item


class Inventory:
    def __init__(self):
        self.stock = {"apple": 10, "banana": 0}

    def take(self, item, quantity):
        if item not in self.stock:
            raise UnknownItemError(item)
        available = self.stock[item]
        if quantity > available:
            raise OutOfStockError(item, quantity, available)
        self.stock[item] -= quantity
        return quantity


inventory = Inventory()

# Handling one very specific case, using its extra data
try:
    inventory.take("banana", 3)
except OutOfStockError as e:
    print(f"Out of stock: need {e.requested}, have {e.available}")

# Handling expected failures from this inventory family
try:
    inventory.take("pear", 1)
except InventoryError as e:
    print("Inventory problem:", e)

# A successful case
taken = inventory.take("apple", 4)
print(f"Took {taken} apples, {inventory.stock['apple']} left")
