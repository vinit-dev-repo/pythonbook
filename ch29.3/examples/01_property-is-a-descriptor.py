# Using @property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value


# The same thing, as a hand-written descriptor
class RadiusDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        instance.__dict__[self.private_name] = value

class Circle2:
    radius = RadiusDescriptor()

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle2(5)
print(c1.radius, c2.radius)

try:
    c1.radius = -1
except ValueError as e:
    print("Circle:", e)

try:
    c2.radius = -1
except ValueError as e:
    print("Circle2:", e)
