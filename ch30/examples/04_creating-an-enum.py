from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

favorite = Color.RED
print(favorite)
print(favorite.name)
print(favorite.value)
