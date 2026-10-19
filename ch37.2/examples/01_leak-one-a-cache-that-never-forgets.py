_cache = {}

def price_with_tax(product_id, price):
    if product_id not in _cache:
        _cache[product_id] = price * 1.2
    return _cache[product_id]

for product_id in range(100_000):
    price_with_tax(product_id, 10.0)

print("things remembered:", len(_cache))
