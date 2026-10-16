import itertools

prices = [10, 20, 30]
tax_rate = itertools.repeat(0.2)
with_tax = map(lambda price, rate: price * (1 + rate), prices, tax_rate)
print(list(with_tax))
