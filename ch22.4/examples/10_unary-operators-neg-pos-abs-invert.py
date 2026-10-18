import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

v = Vector(3, -4)
print(-v)
print(+v)
print(abs(v))

try:
    print(~v)
except TypeError as e:
    print(f"TypeError: {e}")
