import itertools

# 1
print(list(itertools.islice(itertools.count(7, 7), 4)))

# 2
stock = [True, False, True, True, False]
items = ["pen", "cup", "book", "lamp", "bag"]
print(list(itertools.compress(items, stock)))

# 3
temps = [15, 16, 18, 22, 19, 14]
print(list(itertools.takewhile(lambda t: t < 20, temps)))

# 4
print(list(itertools.filterfalse(lambda t: t < 20, temps)))
print(list(itertools.dropwhile(lambda t: t < 20, temps)))
