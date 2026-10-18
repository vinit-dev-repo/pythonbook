# 1
def numbers():
    for n in range(1, 11):
        yield n

def evens_only(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

print(list(evens_only(numbers())))

# 2
def flatten_once(nested):
    for item in nested:
        if isinstance(item, list):
            yield from item
        else:
            yield item

print(list(flatten_once([1, [2, 3], 4, [5]])))

# 3
def read_until(items, stop):
    count = 0
    for item in items:
        if item == stop:
            return count
        yield item
        count += 1
    return count

reader = read_until(["a", "b", "END", "c"], "END")
print(next(reader))
print(next(reader))
try:
    next(reader)
except StopIteration as end:
    print("count:", end.value)

def wrapper(items):
    total = yield from read_until(items, "END")
    yield f"total {total}"

print(list(wrapper(["x", "y", "END", "z"])))

# 4
def broken():
    yield next(iter(()))

try:
    list(broken())
except RuntimeError as error:
    print(type(error).__name__, type(error.__cause__).__name__)
