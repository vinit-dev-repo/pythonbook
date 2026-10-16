for value in (True, "high", float("nan"), float("inf")):
    try:
        p.rating = value
    except (TypeError, ValueError) as error:
        print(repr(value), type(error).__name__)
print("retained:", p.rating)
