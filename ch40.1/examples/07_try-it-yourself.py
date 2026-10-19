# 1
try:
    bad = {1, [1, 2]}
except TypeError as error:
    print("TypeError:", error)

# 2
from_string = set("hello")
from_list = set([1, 2, 2, 3, 3, 3])
empty = set()
print(sorted(from_string))
print(sorted(from_list))
print(empty, type(empty).__name__, type({}).__name__)

# 3
amy = {"apple", "banana", "cherry"}
ben = {"banana", "pear"}
print(sorted(amy.union(ben)))
print(sorted(amy.intersection(ben)))
print(sorted(amy - ben))

# 4
big_list = list(range(1000))
big_set = set(big_list)
print(999 in big_list, 999 in big_set)
print(1000 in big_list, 1000 in big_set)
