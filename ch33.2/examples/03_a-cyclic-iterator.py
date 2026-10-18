class Cycle:
    def __init__(self, values):
        self._values = list(values)
        if not self._values:
            raise ValueError("Cycle needs at least one value")
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self._values[self._index % len(self._values)]
        self._index += 1
        return value

turns = Cycle(["Alice", "Bob", "Cara"])
it = iter(turns)
for _ in range(5):
    print(next(it))
