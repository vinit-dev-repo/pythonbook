# 1
# An iterable is accepted by iter(). A re-iterable container can supply a
# fresh iterator each time. An iterator is also iterable: iter(it) returns it,
# and it keeps one traversal position that iter(it) does not restart.

# 2
it = iter([1, 2])
print(sum(it))     # sum() walked the whole iterator
print(list(it))    # nothing left

# 3
letters = iter("hi")
while True:
    try:
        ch = next(letters)
    except StopIteration:
        break
    print(ch)
try:
    next(letters)
except StopIteration:
    print("exhausted: StopIteration")
