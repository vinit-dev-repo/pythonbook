import math

class CachedCircle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if type(value) not in (int, float):
            raise TypeError("radius must be an int or float, not bool")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("radius must be finite")
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            candidate = math.pi * self.radius ** 2
            if not math.isfinite(candidate):
                raise ValueError("area must be finite")
            self._area = candidate
        return self._area

circle = CachedCircle(2)
print(circle._area is None)
print(round(circle.area, 2))
print(round(circle.area, 2))
circle.radius = 0
print(circle._area is None)
print(circle.area)
print(circle.area)
