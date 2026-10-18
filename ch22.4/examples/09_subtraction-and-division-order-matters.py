class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __sub__(self, scalar):
        return Vector(self.x - scalar, self.y - scalar)

    def __rsub__(self, scalar):
        return Vector(scalar - self.x, scalar - self.y)

v = Vector(2, 3)
print(v - 1)
print(1 - v)
