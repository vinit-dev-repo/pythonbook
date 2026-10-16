from functools import reduce

print(reduce(lambda acc, n: acc + n, [], 0))
try:
    reduce(lambda acc, n: acc + n, [])
except TypeError:
    print("TypeError: no items and no initial value")
