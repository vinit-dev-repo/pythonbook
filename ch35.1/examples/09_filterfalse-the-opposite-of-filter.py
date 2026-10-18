import itertools

numbers = [1, -2, 3, -4, 5]
negatives = itertools.filterfalse(lambda n: n > 0, numbers)
print(list(negatives))
