Point = namedtuple("Point", "x y")
print(Point.__doc__)          # auto-generated

Point.__doc__ = "A point in 2-D space."
print(Point.__doc__)          # your own
