class Direction(Enum):
    NORTH = 1
    UP = 1        # same value as NORTH -> alias, not a new member
    SOUTH = 2

print(Direction.UP)
print(Direction.UP is Direction.NORTH)
