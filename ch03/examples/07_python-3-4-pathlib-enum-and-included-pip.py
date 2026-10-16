from enum import Enum

class Colour(Enum):
    RED = 1
    GREEN = 2

print(Colour.RED)
print(Colour.RED.name, Colour.RED.value)
print(Colour(2))
