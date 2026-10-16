from dataclasses import dataclass
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "x y")
Dimensions = namedtuple("Dimensions", "width height")
print("tuple-style equality:", Coordinate(3, 4) == Dimensions(3, 4))

@dataclass
class Ticket:
    number: int
    title: str

    def label(self):
        return f"#{self.number}: {self.title}"

@dataclass
class ArchivedTicket:
    number: int
    title: str

first = Ticket(7, "Fix docs")
same_fields = Ticket(7, "Fix docs")
other_class = ArchivedTicket(7, "Fix docs")

print("same class, same fields:", first == same_fields)
print("different class, same fields:", first == other_class)
print("same object:", first is same_fields)
print("method:", first.label())
