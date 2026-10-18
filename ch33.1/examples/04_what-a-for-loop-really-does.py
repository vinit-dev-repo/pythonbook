numbers = [1, 2, 3]

# The short way
for n in numbers:
    print("short:", n)

# The long way -- the main iteration steps, written in Python
it = iter(numbers)
while True:
    try:
        n = next(it)
    except StopIteration:
        break
    print("long:", n)
