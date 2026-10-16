from dataclasses import dataclass, field

@dataclass
class Delivery:
    copies: int = 1
    destination: str = field(kw_only=True)

first = Delivery(destination="desk")
second = Delivery(3, destination="shelf")
print(first.copies, first.destination)
print(second.copies, second.destination)
try:
    Delivery(3, "shelf")
except TypeError:
    print("destination needs a keyword")
