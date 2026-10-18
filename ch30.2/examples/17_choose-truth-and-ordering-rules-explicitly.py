from enum import Enum
from functools import total_ordering

@total_ordering
class Ranked(Enum):
    def __lt__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.value < other.value

    def __repr__(self):
        return f'{type(self).__name__}.{self.name}[{self.value}]'

class Urgency(Ranked):
    HIGH = 30
    LOW = 10
    MEDIUM = 20

class Size(Ranked):
    SMALL = 10
    LARGE = 20

print(list(Urgency))
print(sorted(Urgency))
print(Urgency.LOW <= Urgency.LOW, Urgency.HIGH > Urgency.MEDIUM)
print(Urgency.LOW == 10, Urgency.LOW == Size.SMALL)
print({Urgency.LOW: 'queued'}[Urgency.LOW])
for other in (10, Size.SMALL):
    try:
        print(Urgency.LOW < other)
    except TypeError as error:
        print(type(error).__name__)
