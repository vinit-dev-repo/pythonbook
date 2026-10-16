# 1
def count_up(n):
    print("generator body starting")
    for i in range(1, n + 1):
        yield i

gen = count_up(3)
print("created -- nothing printed yet")
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

print(list(islice(powers_of_two(), 6)))   # [1, 2, 4, 8, 16, 32]

# 3
import sys
list_version = [x for x in range(100_000)]
gen_version = (x for x in range(100_000))
print(sys.getsizeof(list_version))   # a large number
print(sys.getsizeof(gen_version))     # a small, roughly fixed number

# 4
def numbers():
    for n in range(1, 11):
        yield n

def evens_only(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

print(list(evens_only(numbers())))   # [2, 4, 6, 8, 10]

# 5
def flatten_once(nested):
    for item in nested:
        if isinstance(item, list):
            yield from item
        else:
            yield item

print(list(flatten_once([1, [2, 3], 4, [5]])))   # [1, 2, 3, 4, 5]
