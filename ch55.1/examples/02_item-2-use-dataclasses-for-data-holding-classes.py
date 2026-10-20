from dataclasses import dataclass  # @dataclass needs Python 3.7+

@dataclass(frozen=True)
class Point:
    x: float
    y: float = 0.0        # a field default

p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1)
print(p1 == p2)
