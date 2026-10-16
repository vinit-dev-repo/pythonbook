from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda acc, n: acc + n, numbers)
print(total)
