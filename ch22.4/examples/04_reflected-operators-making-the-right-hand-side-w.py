class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(2, 3)
print(v * 2)     # Vector.__mul__(v, 2) - works
try:
    print(2 * v)     # int.__mul__(2, v) declines, Vector has no __rmul__
except TypeError as e:
    print(f"TypeError: {e}")
