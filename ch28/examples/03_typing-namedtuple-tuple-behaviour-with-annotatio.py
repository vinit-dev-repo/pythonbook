from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

p = Point(3, 4)
print(p)
print(p.x)
