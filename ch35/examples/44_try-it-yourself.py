import itertools

# 1
print(list(itertools.islice(itertools.count(7, 7), 4)))   # [7, 14, 21, 28]

# 2
stock = [True, False, True, True, False]
items = ["pen", "cup", "book", "lamp", "bag"]
print(list(itertools.compress(items, stock)))              # ['pen', 'book', 'lamp']

# 3
temps = [15, 16, 18, 22, 19, 14]
print(list(itertools.takewhile(lambda t: t < 20, temps)))  # [15, 16, 18]

# 4
records = [("red", 5), ("blue", 3), ("red", 2), ("blue", 7)]
records_sorted = sorted(records, key=lambda r: r[0])
for colour, group in itertools.groupby(records_sorted, key=lambda r: r[0]):
    print(colour, sum(n for _, n in group))
# blue 10
# red 7

# 5
letters = ["A", "B", "C"]
ordered = list(itertools.permutations(letters, 2))
unordered = list(itertools.combinations(letters, 2))
print(ordered)     # [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]  -> 6
print(unordered)   # [('A','B'), ('A','C'), ('B','C')]                                    -> 3
# permutations counts A-then-B and B-then-A as different; combinations treats them as the same pair.
