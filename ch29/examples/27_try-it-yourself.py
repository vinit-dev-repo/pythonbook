# 1 and 3
class NonEmptyString:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.private_name not in instance.__dict__:
            raise AttributeError(self.private_name[1:])
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if type(value) is not str:
            raise TypeError("must be a built-in string")
        if value == "":
            raise ValueError("must not be empty")
        instance.__dict__[self.private_name] = value

class Book:
    title = NonEmptyString()
    def __init__(self, title):
        self.title = title

b = Book("Dune")
print(b.title)          # Dune

# 2
# Because self.value lives on the ONE shared PositiveNumber object,
# not on each Product instance -- every Product reads/writes the same slot.

# 4
class Locked:
    def __get__(self, instance, owner):
        return "descriptor wins"
    def __set__(self, instance, value):
        pass  # a data descriptor just needs __set__ to exist

class Demo:
    x = Locked()

d = Demo()
d.__dict__["x"] = 99          # sneak a value directly into __dict__
print(d.x)                     # "descriptor wins" -- selected data descriptor has __get__

# 5
from functools import cached_property
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("  (computing area ...)")
        return math.pi * self.radius ** 2

c = Circle(3)
print(c.area)   # computes
print(c.area)   # cached, no "(computing area ...)" line
