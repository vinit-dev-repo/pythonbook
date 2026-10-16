class LazySquares:
    """Produces squares 0, 1, 4, 9, ... up to `limit`, ONE AT A TIME."""

    def __init__(self, limit):
        self._limit = limit

    def __iter__(self):
        return LazySquaresIterator(self._limit)


class LazySquaresIterator:
    def __init__(self, limit):
        self._limit = limit
        self._n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._n >= self._limit:
            raise StopIteration
        value = self._n * self._n     # only computed NOW, not stored ahead of time
        self._n += 1
        return value

for sq in LazySquares(5):
    print(sq)
