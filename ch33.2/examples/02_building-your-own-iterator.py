class Countdown:
    """Counts down from `start` to 1, then stops."""

    def __init__(self, start):
        self._current = start

    def __iter__(self):
        return self          # an iterator's __iter__ returns itself

    def __next__(self):
        if self._current <= 0:
            raise StopIteration
        value = self._current
        self._current -= 1
        return value

for n in Countdown(3):
    print(n)
