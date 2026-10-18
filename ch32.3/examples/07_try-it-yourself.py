# 1
class Countdown:
    def __init__(self, start):
        self._start = start

    def __len__(self):
        return self._start

    def __getitem__(self, index):
        if not 0 <= index < self._start:
            raise IndexError("countdown index out of range")
        return self._start - index

print(list(Countdown(3)))
print(Countdown(3)[1], len(Countdown(3)))
print(4 in Countdown(3))

# 2
class Percents:
    def __init__(self, values):
        items = tuple(values)
        if any(type(item) is not int for item in items):
            raise TypeError("percents must be built-in integers")
        if any(not 0 <= item <= 100 for item in items):
            raise ValueError("percents must be between 0 and 100")
        self._items = items

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return Percents(result) if isinstance(index, slice) else result

    def __repr__(self):
        return f"Percents({self._items})"

print(Percents([5, 50, 100])[1:])
for bad in ([True], [101]):
    try:
        Percents(bad)
    except (TypeError, ValueError) as error:
        print(type(error).__name__, error)

# 3
class Bag:
    def __init__(self, items):
        self._items = list(items)

    def __add__(self, other):
        return Bag(self._items + list(other))

    def __iadd__(self, other):
        self._items += list(other)
        return self

    def __mul__(self, times):
        return Bag(self._items * times)

    def __repr__(self):
        return f"Bag({self._items})"

bag = Bag([1, 2])
same = bag
bigger = bag + [3]
print(bigger, bigger is bag)
bag += [3]
print(same, bag is same)
print(bag * 2)
