# counted_sequence_fragment.py
class CountedValues(Fibonacci):
    total_adds = 0

    def __init__(self, values):
        super().__init__(values)
        self.adds = 0

    def __add__(self, other):
        result = super().__add__(other)
        self.adds += 1
        CountedValues.total_adds += 1
        print("successful add", self.adds)
        return result

    def __getattr__(self, name):
        if name in {"sort", "reverse"}:
            return getattr(self._values, name)
        raise AttributeError(name)

seed = [4, 1]
first = CountedValues(seed)
second = CountedValues(first)
seed.append(9)
print(list(first), list(second))
first.append(3)
first.sort()
first.reverse()
print(list(first), list(second))
result = first + [7]
second + [8]
first + []
print(first.adds, second.adds, CountedValues.total_adds)
print(type(result).__name__, list(result))
try:
    [0] + first
except TypeError:
    print("reflected addition not supplied")
