from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "I am a shape"

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def describe(self):
        return "I am a square"

    def area(self):
        return self.side ** 2

# 1 and 2
sq = Square("Sq1", 4)
print(sq.describe())
print(sq.name, sq.area())

# 3
try:
    s = Shape("generic")
except TypeError as e:
    print("Failed as expected:", e)

# 4
class Car:
    def move(self):
        return "drives"

class Boat:
    def move(self):
        return "sails"

for thing in [Car(), Boat()]:
    print(thing.move())

# 5
print(Square.__mro__)
