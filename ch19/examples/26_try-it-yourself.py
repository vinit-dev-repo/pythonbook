from collections import namedtuple

# 1
book = ("Dune", "Frank Herbert", 1965)
title, author, year = book
print(f"{title} was written by {author} in {year}.")

# 2
Book = namedtuple("Book", "title author year")
b = Book("Dune", "Frank Herbert", 1965)
print(b)
print(b.author)              # Frank Herbert

# 3
b2 = b._replace(year=2021)   # e.g. a reprint edition
print(b2)                    # year=2021
print(b)                     # original still year=1965

# 4
MinMax = namedtuple("MinMax", "low high")

def min_max(numbers):
    return MinMax(min(numbers), max(numbers))

print(min_max([4, 8, 15, 16, 23, 42]))   # MinMax(low=4, high=42)
