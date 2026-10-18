import math
from functools import cached_property


# 1
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("must be positive")
        instance.__dict__[self.private_name] = value


class Shape:
    size = Positive()

    def __init__(self, size):
        self.size = size


class Square(Shape):
    pass


class Loose(Shape):
    size = 0


print("size" in vars(Square), Square(3).size)
try:
    Square(-1)
except ValueError as error:
    print(error)
print(Loose(-5).size)


# 2
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.private_name[1:]} must be of type {self.expected_type.__name__}")
        instance.__dict__[self.private_name] = value


class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


ada = Person("Ada", 36)
print(ada.name, ada.age)
try:
    Person("Lin", "x")
except TypeError as error:
    print(error)


# 3
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("  (computing area ...)")
        return math.pi * self.radius ** 2


c = Circle(3)
print(c.area)
print(c.area)
