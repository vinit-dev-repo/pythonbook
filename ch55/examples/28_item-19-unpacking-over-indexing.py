point = (3, 4)

# indexing
x = point[0]
y = point[1]

# unpacking — Pythonic
x, y = point
print(x, y)

first, *rest = [1, 2, 3, 4]
print(first, rest)
