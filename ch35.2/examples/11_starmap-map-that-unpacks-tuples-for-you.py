combined = map(lambda a, b: a + b, [3, 5], [10], strict=True)
print(next(combined))
try:
    next(combined)
except ValueError:
    print("unequal input lengths")
