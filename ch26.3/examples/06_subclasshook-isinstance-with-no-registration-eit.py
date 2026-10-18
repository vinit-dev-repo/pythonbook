from collections.abc import Iterable

class MyStream:
    """Does not inherit from Iterable and is never registered."""
    def __iter__(self):
        return iter([1, 2, 3])

print(isinstance(MyStream(), Iterable))
print(issubclass(MyStream, Iterable))
