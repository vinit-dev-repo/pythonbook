names = ["apple", "bread", "milk"]
prices = [0.5, 2.2, 1.1]

price_lookup = {name: price for name, price in zip(names, prices)}
print(price_lookup)
