# c3_order.py
class Stored:
    pass

class Cached(Stored):
    pass

class Printable:
    pass

class Dashboard(Cached, Printable):
    pass

print([cls.__name__ for cls in Dashboard.__mro__])

class StoreFirst(Stored, Printable):
    pass

class PrintFirst(Printable, Stored):
    pass

try:
    class Conflicted(StoreFirst, PrintFirst):
        pass
except TypeError:
    print("inconsistent order rejected")
