# 1
from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Segment:
    length: float

    def __post_init__(self):
        if type(self.length) not in (int, float) or self.length <= 0:
            raise ValueError("length must be a positive int or float")


class SegmentWalk:
    def __init__(self, limit):
        self._limit = limit

    def __iter__(self):
        return (Segment(n) for n in range(1, self._limit + 1))

walk = SegmentWalk(3)
first, second = iter(walk), iter(walk)
print(next(first), next(first), next(second))
print(list(first), list(first))

# 2
@dataclass(frozen=True)
class CachedSegment(Segment):
    @cached_property
    def double(self):
        print("computing")
        return self.length * 2

segment = CachedSegment(4)
print(sorted(vars(segment)))
print(segment.double, segment.double)
print(sorted(vars(segment)))

# 3
try:
    walk[0]
except TypeError as error:
    print(error)
print(list(walk)[0])
