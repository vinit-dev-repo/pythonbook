Other = namedtuple("Other", "left right")
print(Point(1, 2) == (1, 2))
print(Point(1, 2) == Other(1, 2))
print(Point("east", None))
