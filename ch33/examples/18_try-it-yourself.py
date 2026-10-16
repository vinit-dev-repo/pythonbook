# 1
class Evens:
    def __init__(self):
        self._n = 0
    def __iter__(self):
        return self
    def __next__(self):
        value = self._n
        self._n += 2
        return value

it = iter(Evens())
for _ in range(5):
    print(next(it))

# 2
# An iterable is accepted by iter(). A re-iterable container can supply a
# fresh iterator, but an iterator is also iterable: iter(it) returns it.
# That iterator keeps one traversal position; iter(it) does not restart it.

# 3
it = iter([1, 2])
print(sum(it))     # 3 -- sum() walked the whole iterator
print(list(it))    # [] -- nothing left

# 4
class Deck:
    def __init__(self):
        self._cards = ["A", "B", "C", "D"]
    def __iter__(self):
        return iter(self._cards)

deck = Deck()
for c in deck:
    print("first loop:", c)
for c in deck:
    print("second loop:", c)   # works again -- fresh iterator each time

# 5
rolls = [2, 4, 1, 6, 3]
_state = {"i": 0}
def fake_roll():
    value = rolls[_state["i"]]
    _state["i"] += 1
    return value

for roll in iter(fake_roll, 6):
    print(roll)
