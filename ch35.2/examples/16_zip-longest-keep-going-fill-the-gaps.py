import itertools

names = ["Ann", "Bo", "Cy"]
scores = [90, 85]

print(list(itertools.zip_longest(names, scores, fillvalue="—")))
