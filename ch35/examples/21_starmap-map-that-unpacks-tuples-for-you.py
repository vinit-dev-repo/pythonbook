import itertools

pairs = [(2, 3), (4, 5), (6, 7)]

# Multi-input map: corresponding positions from two separate lists
a_values = [2, 4, 6]
b_values = [3, 5, 7]
via_zip_map = list(map(lambda a, b: a * b, a_values, b_values))

# The starmap way: one list of ready-made pairs
via_starmap = list(itertools.starmap(lambda a, b: a * b, pairs))

print(via_zip_map)
print(via_starmap)
