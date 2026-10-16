from enum import Enum

class CustomEquality(Enum):
    ITEM = 1

    def __eq__(self, other):
        return self is other

print(CustomEquality.ITEM == CustomEquality.ITEM)
try:
    hash(CustomEquality.ITEM)
except TypeError as error:
    print(type(error).__name__)
