# 1
n = 10
before = id(n)
n = n + 1
print(id(n) == before)       # False: n now refers to the result, 11
items = [1, 2, 3]
before = id(items)
items.append(4)
print(id(items) == before)   # True: the same list changed in place

# 2
a = [1, 2]
b = a
b.append(3)
print(a, b, a is b)          # [1, 2, 3] [1, 2, 3] True

# 3
a = [1, 2]
b = a.copy()
b.append(3)
print(a, b, a is b)          # [1, 2] [1, 2, 3] False

# 4
rows = [[0] * 2] * 2
rows[0][1] = 9
print(rows)                  # [[0, 9], [0, 9]]

rows = [[0] * 2 for _ in range(2)]
rows[0][1] = 9
print(rows)                  # [[0, 9], [0, 0]]

rows = [([],) for _ in range(2)]
rows[0][0].append('x')
print(rows)                  # [(['x'],), ([],)]
