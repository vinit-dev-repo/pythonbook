import itertools

def is_odd(n):
    return n % 2 == 1

numbers = [1, 3, 5, 4, 7, 2]

print(list(itertools.takewhile(is_odd, numbers)))
print(list(itertools.dropwhile(is_odd, numbers)))
print(list(filter(is_odd, numbers)))
