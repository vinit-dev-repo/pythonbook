from typing import Protocol, runtime_checkable


# 1
@runtime_checkable
class SupportsArea(Protocol):
    def area(self) -> float: ...


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


print(isinstance(Square(4), SupportsArea))

# 2
print(
    "In these examples, registration or a runtime Protocol match provides "
    "recognition without inheriting methods from that ABC or Protocol."
)


# 3
class Broken:
    area = "big"


print(isinstance(Broken(), SupportsArea))
try:
    Broken().area()
except TypeError as error:
    print(error)
