from enum import Enum

class Size(Enum):
    SMALL = "S"
    LARGE = "L"

try:
    class MoreSizes(Size):
        pass
except TypeError as error:
    print(type(error).__name__)
