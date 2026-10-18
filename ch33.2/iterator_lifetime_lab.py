# iterator_lifetime_lab.py
class NumberBag:
    """The ITERABLE -- holds the data."""

    def __init__(self, values):
        self._values = list(values)

    def __iter__(self):
        return NumberBagIterator(self._values)   # a FRESH iterator every time

class NumberBagIterator:
    """The ITERATOR -- remembers position for ONE pass."""

    def __init__(self, values):
        self._values = values
        self._index = 0
        self._exhausted = False

    def __iter__(self):
        return self

    def __next__(self):
        if self._exhausted:
            raise StopIteration
        if self._index >= len(self._values):
            self._exhausted = True
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value

bag = NumberBag([10, 20, 30])

for a in bag:
    for b in bag:                 # a SECOND, independent loop over the same bag
        print(a, b)

values = [1]
old = NumberBagIterator(values)
print('yield:', next(old))
try:
    next(old)
except StopIteration:
    print('terminal: StopIteration')
values.append(2)
try:
    next(old)
except StopIteration:
    print('old after append: StopIteration')
print('fresh:', list(NumberBagIterator(values)))
