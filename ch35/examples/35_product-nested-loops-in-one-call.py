import itertools

sizes = ["S", "M", "L"]
colours = ["red", "blue"]

for size, colour in itertools.product(sizes, colours):
    print(size, colour)
