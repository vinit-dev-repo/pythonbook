# 1
def area_of_square(side):
    """Return the area of a square with the given side."""
    return side ** 2

help(area_of_square)

# 2
print([name for name in dir([]) if not name.startswith("_") and name.startswith("s")])   # ['sort']

# 3
def add(a: int, b: int) -> int:
    return a + b

print(add("2", "3"))   # 23: annotations are not enforced, so the strings are joined
