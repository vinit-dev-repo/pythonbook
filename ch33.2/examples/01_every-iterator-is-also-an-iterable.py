numbers = [1, 2, 3]
it = iter(numbers)
print(iter(it) is it)   # True -- an iterator's __iter__ returns itself
