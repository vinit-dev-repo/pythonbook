# call_timings.py
from functools import wraps
from time import perf_counter

def call_timings(*, label="call", trace=False, clock=perf_counter):
    def decorate(func):
        @wraps(func)
        def call(*args, **kwargs):
            start = clock()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed = clock() - start
                call.stats["calls"] += 1
                call.stats["last"] = elapsed
                call.stats["total"] += elapsed
                if trace:
                    print(f"{label}: {elapsed:.6f}s")
        call.stats = {"calls": 0, "last": 0.0, "total": 0.0}
        return call
    return decorate

@call_timings()
def joined(left, *, right):
    return left + right

class Batch:
    def __init__(self, name):
        self.name = name

    @call_timings(label="batch")
    def take(self, amount):
        if amount < 0:
            raise ValueError("negative amount")
        return self.name, amount

print(joined("a", right="b"))
east, west = Batch("east"), Batch("west")
saved = east.take
print(west.take(2), saved(1))
try:
    east.take(-1)
except ValueError:
    print("target failure preserved")
print(joined.stats["calls"], Batch.take.stats["calls"])
print(Batch.take.stats["total"] >= Batch.take.stats["last"] >= 0)
print(joined.stats is Batch.take.stats)
