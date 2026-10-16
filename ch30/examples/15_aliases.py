from enum import Enum, unique

try:
    @unique
    class Direction(Enum):
        NORTH = 1
        UP = 1
        SOUTH = 2
except ValueError as e:
    print(e)
