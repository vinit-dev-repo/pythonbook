class PublicRadius:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

class GetterOnlyRadius(PublicRadius):
    @property
    def radius(self):
        return self._radius

try:
    GetterOnlyRadius(1)
except AttributeError:
    print("AttributeError: child property has no setter")

import math

class ValidatedRadius:
    def __init__(self, radius):
        self._set_radius(radius)

    def _set_radius(self, value):
        if type(value) not in (int, float):
            raise TypeError("radius must be a built-in int or float")
        if value <= 0 or (type(value) is float and not math.isfinite(value)):
            raise ValueError("radius must be positive and finite")
        self._radius = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._set_radius(value)

class UnitRadius(ValidatedRadius):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return self._radius

unit_radius = UnitRadius()
print(unit_radius.radius)
try:
    unit_radius.radius = 2
except AttributeError:
    print("AttributeError: public radius is read-only")
ordinary_radius = ValidatedRadius(2)
try:
    ordinary_radius.radius = float("inf")
except ValueError:
    print("ValueError: invalid radius; stored value unchanged")
print(ordinary_radius.radius)
