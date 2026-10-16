from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    DONE = auto()

for s in Status:
    print(s.name, s.value)
