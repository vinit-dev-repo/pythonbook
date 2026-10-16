import functools

@functools.lru_cache(maxsize=1000)
def price_with_tax(product_id, price):
    return price * 1.2

for product_id in range(100_000):
    price_with_tax(product_id, 10.0)

print("things remembered:", price_with_tax.cache_info().currsize)
