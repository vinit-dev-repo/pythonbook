for quantity in (-1, True, 1.5, float("nan"), 0):
    trial = Inventory()
    trial.take("apple", quantity)
    print(repr(quantity), "leaves", trial.stock["apple"])
