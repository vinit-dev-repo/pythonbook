# base_paths.py
def show_base_paths(cls, depth=0):
    print("  " * depth + cls.__name__)
    for base in cls.__bases__:
        show_base_paths(base, depth + 1)


class Asset:
    pass


class Tagged(Asset):
    pass


class Cached(Asset):
    pass


class Report(Tagged, Cached):
    pass


show_base_paths(Report)
print("lookup:", " -> ".join(cls.__name__ for cls in Report.__mro__))
