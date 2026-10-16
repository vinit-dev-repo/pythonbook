trial = Inventory()
try:
    trial.take("pear", -1)
except InventoryError as error:
    print(type(error).__name__)
print(trial.stock)
print(trial.take("apple", 10), trial.stock["apple"])
