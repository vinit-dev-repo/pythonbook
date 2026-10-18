from enum import Enum

class PlainGate(Enum):
    CLOSED = 0
    OPEN = 1

class Gate(Enum):
    CLOSED = 0
    OPEN = 1

    def __bool__(self):
        return self is Gate.OPEN

print(bool(PlainGate.CLOSED), bool(PlainGate.CLOSED.value))
print(bool(Gate.CLOSED), bool(Gate.OPEN))
print(Gate(0) is Gate.CLOSED)
