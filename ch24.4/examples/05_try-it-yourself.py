class InventoryError(Exception):
    pass

class UnknownItemError(InventoryError):
    pass

class InvalidQuantityError(InventoryError):
    pass

class OutOfStockError(InventoryError):
    def __init__(self, item, requested, available):
        super().__init__(f"{item}: requested {requested}, available {available}")
        self.item = item
        self.requested = requested
        self.available = available

class Inventory:
    def __init__(self, stock):
        self.stock = dict(stock)

    def take(self, item, quantity):
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
            raise InvalidQuantityError(f"invalid quantity: {quantity!r}")
        if item not in self.stock:
            raise UnknownItemError(item)
        if quantity > self.stock[item]:
            raise OutOfStockError(item, quantity, self.stock[item])
        self.stock[item] -= quantity

# 1
inventory = Inventory({"apple": 10})
try:
    inventory.take("apple", 12)
except OutOfStockError as error:
    print(error.requested, error.available)    # 12 10
except InventoryError:
    print("another inventory problem")

# 2
for bad in (-1, True, 1.5, 0):
    try:
        inventory.take("apple", bad)
    except InvalidQuantityError as error:
        print(error)
# invalid quantity: -1
# invalid quantity: True
# invalid quantity: 1.5
# invalid quantity: 0
print(inventory.stock)                         # {'apple': 10}

# 3
try:
    inventory.take("pear", -1)
except InventoryError as error:
    print(type(error).__name__)                # InvalidQuantityError
