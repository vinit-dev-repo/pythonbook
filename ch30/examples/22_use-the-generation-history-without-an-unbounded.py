from enum import Enum, auto

class Counters(Enum):
    LARGE = 9
    SMALL = 2
    NEXT = auto()

print(Counters.NEXT.value)
try:
    class Mixed(Enum):
        WORD = 'word'
        NUMBER = auto()
except TypeError as error:
    print(type(error).__name__)
