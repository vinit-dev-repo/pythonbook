def get_item(items, name):
    if name not in items:
        raise NotFoundError(f"No item called {name!r}")
    return items[name]

def check_price(price):
    if price < 0:
        raise ValidationError(f"Price cannot be negative: {price}")

try:
    get_item({}, "widget")
except AppError as e:
    print("Caught as AppError:", e)

try:
    check_price(-5)
except AppError as e:
    print("Caught as AppError:", e)
