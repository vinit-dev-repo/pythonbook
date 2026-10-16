import itertools

original = iter([1, 2, 3, 4])
copy_a, copy_b = itertools.tee(original, 2)

print(list(copy_a))
print(list(copy_b))
