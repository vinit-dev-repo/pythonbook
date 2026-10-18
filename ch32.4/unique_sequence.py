# unique_sequence.py
class UniqueSequence:
    def __init__(self, values=()):
        self._values = []
        for value in values:
            self.add(value)

    def add(self, value):
        if value not in self._values:
            self._values.append(value)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __iter__(self):
        return iter(self._values)

    def __repr__(self):
        return f"UniqueSequence({self._values!r})"

    def union(self, other):
        result = UniqueSequence(self)
        for value in other:
            result.add(value)
        return result

    def intersection(self, other):
        pool = tuple(other)
        return UniqueSequence(value for value in self if value in pool)

    def __or__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

class ManyUnique(UniqueSequence):
    def union(self, *others):
        result = UniqueSequence(self)
        for other in others:
            for value in other:
                result.add(value)
        return result

    def intersection(self, *others):
        pools = [tuple(other) for other in others]
        return UniqueSequence(
            value for value in self
            if all(value in pool for pool in pools)
        )

if __name__ == "__main__":
    letters = ManyUnique("level")
    print(letters)
    print(letters[0], letters[-1], letters[1:])
    print(letters & "velvet")
    print(letters | "echo")
    print(letters.intersection(iter("velvet"), "olive"))
    print(letters.union("echo", "new"))
    print((letters & "velvet") & "olive")
    print(type(letters.union()).__name__)
    print(list(UniqueSequence([[2], [2], [4]])))
