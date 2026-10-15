# split_check.py
items = ["a", "b", "c", "d", "e"]
midpoint = len(items) // 2
left = items[:midpoint]
right = items[midpoint:]
assert len(left) + len(right) == len(items), "split lost an item"
print(left, right)
