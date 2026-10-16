import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if type(value) not in (int, float):
            raise TypeError("radius must be an int or float, not bool")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("radius must be finite")
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    radius = property(get_radius, set_radius, None, "The circle's radius.")

c = Circle(3)
print(c.radius)

c.radius = 10
print(c.radius)

print(Circle.radius.__doc__)
