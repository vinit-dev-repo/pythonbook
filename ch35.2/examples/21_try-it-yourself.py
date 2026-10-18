import itertools

# 1
jobs = ["scan", "print", "mail", "copy", "fax"]
colours = itertools.cycle(["red", "blue"])
for number, job, colour in zip(itertools.count(1), jobs, colours):
    print(number, job, colour)

# 2
days = [["Mon", "Tue"], ["Wed"], ["Thu", "Fri"]]
print(list(itertools.chain.from_iterable(days)))
copy_a, copy_b = itertools.tee(iter([3, 1, 2]))
print(sorted(copy_a), max(copy_b))

# 3
print(list(itertools.starmap(pow, [(2, 3), (3, 2), (10, 0)])))
print(list(itertools.accumulate([3, 1, 4, 1, 5], max)))
print(list(itertools.accumulate([3, 1, 4], initial=100)))

# 4
names = ["Ann", "Bo", "Cy"]
scores = [90, 85]
print(list(itertools.zip_longest(names, scores, fillvalue=0)))
try:
    list(zip(names, scores, strict=True))
except ValueError as error:
    print("strict zip:", error)
