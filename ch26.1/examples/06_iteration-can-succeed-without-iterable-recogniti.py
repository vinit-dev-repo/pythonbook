from collections.abc import Iterable

class CountdownFrom:
    def __init__(self, start):
        self._start = start

    def __getitem__(self, index):
        value = self._start - index
        if value < 0:
            raise IndexError(index)
        return value

cd = CountdownFrom(3)
print("values:", list(cd))
print("Iterable recognition:", isinstance(cd, Iterable))
