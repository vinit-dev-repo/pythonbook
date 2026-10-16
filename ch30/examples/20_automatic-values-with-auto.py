from enum import Enum, auto

class Status(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()   # use the lowercased member NAME as the value

    PENDING = auto()
    ACTIVE = auto()
    DONE = auto()

print(Status.PENDING.value)
print(Status.ACTIVE.value)
