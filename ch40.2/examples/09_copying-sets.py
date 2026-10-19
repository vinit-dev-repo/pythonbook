a = {1, 2, 3}
b = a.copy()
b.add(4)
print(sorted(a), sorted(b))     # a is untouched — separate outer sets
