import math

class Typed:
    """Accepts instances of the chosen type, including its subclasses."""
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
            raise TypeError(
                f"{self.private_name[1:]} must be a {self.expected_type.__name__}"
            )
        instance.__dict__[self.private_name] = value


class Bounded:
    """A descriptor that only accepts numbers inside a range."""
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("value must be an int or float, not bool")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("value must be finite")
        if not (self.minimum <= value <= self.maximum):
            raise ValueError(
                f"{self.private_name[1:]} must be between {self.minimum} and {self.maximum}"
            )
        instance.__dict__[self.private_name] = value


class Employee:
    name = Typed(str)
    age = Bounded(18, 70)
    salary = Bounded(0, 1_000_000)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Product:
    name = Typed(str)
    rating = Bounded(0, 5)

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


e = Employee("Vinit", 30, 55000)
print(e.name, e.age, e.salary)

p = Product("Coffee", 4.5)
print(p.name, p.rating)

try:
    e.age = 15
except ValueError as e_err:
    print(e_err)

try:
    p.name = 123
except TypeError as t_err:
    print(t_err)
