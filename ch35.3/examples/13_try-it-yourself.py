import itertools

# 1
records = [("red", 5), ("blue", 3), ("red", 2), ("blue", 7)]
records_sorted = sorted(records, key=lambda r: r[0])
for colour, group in itertools.groupby(records_sorted, key=lambda r: r[0]):
    print(colour, sum(n for _, n in group))

# 2
letters = ["A", "B", "C"]
ordered = list(itertools.permutations(letters, 2))
unordered = list(itertools.combinations(letters, 2))
print(ordered, len(ordered))
print(unordered, len(unordered))

# 3
print(len(list(itertools.product("ab", repeat=3))))
print(list(itertools.combinations_with_replacement("ab", 2)))

# 4
readings = [5, 9, 8, 13]
print([later - earlier for earlier, later in itertools.pairwise(readings)])
source = iter(readings)
batches = itertools.batched(source, 3, strict=True)
print(next(batches))
try:
    next(batches)
except ValueError:
    print("short final batch")
print(list(source))
