class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v = Vector(2, 3)
print(v + Vector(1, 1))   # Vector.__add__(v, Vector(1, 1)) - works

try:
    print(5 + v)           # int.__add__(5, v) declines, Vector has no __radd__
except TypeError as e:
    print(f"TypeError: {e}")
