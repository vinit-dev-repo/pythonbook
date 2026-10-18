class InventoryError(Exception):
    """Base class for expected inventory failures."""
    pass

class InvalidQuantityError(InventoryError):
    def __init__(self, quantity):
        super().__init__("Quantity must be a positive built-in integer")
        self.quantity = quantity

class OutOfStockError(InventoryError):
    def __init__(self, item, requested, available):
        super().__init__("Insufficient stock for the requested item")
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
        if type(quantity) is not int or quantity <= 0:
            raise InvalidQuantityError(quantity)
        if item not in self.stock:
            raise UnknownItemError(item)
        available = self.stock[item]
        if quantity > available:
            raise OutOfStockError(item, quantity, available)
        self.stock[item] -= quantity
        return quantity

inventory = Inventory()
for item, quantity in (("apple", -1), ("banana", 3), ("pear", 1)):
    before = inventory.stock.copy()
    try:
        inventory.take(item, quantity)
    except InventoryError as error:
        print(type(error).__name__, inventory.stock == before)
taken = inventory.take("apple", 4)
print(f"Took {taken} apples, {inventory.stock['apple']} left")
