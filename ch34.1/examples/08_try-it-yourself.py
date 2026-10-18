# 1
def count_up(n):
    print("generator body starting")
    for i in range(1, n + 1):
        yield i

gen = count_up(3)
print("created, nothing printed yet")
print(next(gen))
print(next(gen))
print(next(gen))

# 2
from itertools import islice

def powers_of_two():
    value = 1
    while True:
        yield value
        value *= 2

print(list(islice(powers_of_two(), 6)))

# 3
class Squares:
    def __init__(self, limit):
        self._limit = limit

    def __iter__(self):
        for n in range(1, self._limit + 1):
            yield n * n

squares = Squares(3)
print(list(squares))
print(list(squares))
print(iter(squares) is iter(squares))
