# 1
book = ("Dune", "Frank Herbert", 1965)
title, author, year = book
print(f"{title} was written by {author} in {year}.")

# 2
trips = [("London", 2024, 8.9), ("Paris", 2023, 9.2), ("Rome", 2022, 8.5)]
for city, year, rating in trips:
    print(f"{city} ({year}): {rating}/10")

# 3
record = ("Ana", [85, 90])
record[1].append(100)
print(record)                         # ('Ana', [85, 90, 100])
try:
    record[0] = "Bea"
except TypeError as error:
    print(error)                      # 'tuple' object does not support item assignment

# 4
locations = {("London", "UK"): "rainy"}
print(locations[("London", "UK")])    # rainy
try:
    bad = {[1, 2]: "oops"}
except TypeError as error:
    print(error)                      # cannot use 'list' as a dict key (unhashable type: 'list')
