from dataclasses import dataclass

@dataclass
class Position:
    x: int
    y: int

@dataclass
class Size:
    width: int
    height: int

p = Position(3, 4)
same_position = Position(3, 4)
size = Size(3, 4)
print(p == size)
print(p == same_position)
print(p is same_position)
