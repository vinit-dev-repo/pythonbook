import itertools

fruits = ["apple", "banana", "cherry", "date"]
in_stock = [True, False, True, True]

available = itertools.compress(fruits, in_stock)
print(list(available))
