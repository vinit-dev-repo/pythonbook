from collections import namedtuple
from fractions import Fraction

BatchStats = namedtuple("BatchStats", "count mean")

def batch_statistics():
    count = 0
    total = 0
    while True:
        mean = Fraction(total, count) if count else None
        item = yield BatchStats(count, mean)
        if item is None:
            return BatchStats(count, mean)
        if type(item) is not int or item < 0:
            raise ValueError("parcel counts must be nonnegative integers")
        total += item
        count += 1

def collect_batches(completed):
    while True:
        completed.append((yield from batch_statistics()))

direct = batch_statistics()
print("initial:", next(direct))
print("running:", direct.send(2))
print("running:", direct.send(5))
try:
    direct.send(None)
except StopIteration as finished:
    print("returned:", finished.value)

completed = []
groups = collect_batches(completed)
print("group initial:", next(groups))
groups.send(3)
groups.send(8)
assert completed == []             # no return from the subgenerator yet
print("next group:", groups.send(None))
print("completed:", completed)
groups.send(None)                  # explicitly finish an empty group
print("empty group:", completed[-1])
groups.close()                     # abandon the new, unfinished group
assert len(completed) == 2
