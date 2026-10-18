import math

# 1
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        top = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(top, self.denominator * other.denominator)

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

print(sum([Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]))   # Fraction(36, 36)

# 2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

v = Vector(2, 3)
v *= 2
print(v)                                       # Vector(4, 6)

class BrokenVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"BrokenVector({self.x}, {self.y})"

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar

broken = BrokenVector(2, 3)
broken *= 2
print(broken)                                  # None

# 3
class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Number(self.value - other)

    def __rsub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Number(other - self.value)

print(Number(3) - 10)                          # Number(-7)
print(10 - Number(3))                          # Number(7)

# 4
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount < other.amount

print(Money(5, "USD") == 5)                    # False
try:
    Money(5, "USD") < 5
except TypeError as error:
    print(type(error).__name__)                # TypeError

# 5
class Arrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Arrow({self.x}, {self.y})"

    def __neg__(self):
        return Arrow(-self.x, -self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

arrow = Arrow(3, 4)
print(-arrow)                                  # Arrow(-3, -4)
print(abs(arrow))                              # 5.0
