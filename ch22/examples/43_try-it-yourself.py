# Public fraction fields are read-only. Do not change the private backing fields.
# For real programs, prefer the standard library's fractions.Fraction.
class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("use integer numerator and denominator")
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __radd__(self, other):
        # sum() starts from 0, so the first call is really 0 + Fraction(...)
        if isinstance(other, int) and other == 0:
            return self
        return self.__add__(other)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __hash__(self):
        # Hash the fraction in LOWEST TERMS, so 1/2 and 2/4 - which __eq__ calls
        # equal - hash the same. Do NOT write hash(self.numerator / self.denominator):
        # that division makes a float, which loses precision for large fractions and
        # raises OverflowError outright on something like Fraction(10**10000, 3).
        from math import gcd
        if self.denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        g = gcd(self.numerator, self.denominator)
        numerator = self.numerator // g
        denominator = self.denominator // g
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        return hash((numerator, denominator))

# 1
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)

# 2
f3 = Fraction(2, 4)
print(f1 == f3)
print(hash(f1) == hash(f3))

# 3
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

p = Playlist()
print(bool(p))
p.add("Song A")
print(bool(p))

# 4
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

double = Multiplier(2)
print(double(5))

# 1 continued: repr inside a container
print([f1])

# 5
fractions = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
print(sum(fractions))

# 6
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
print(v)

class BrokenVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"BrokenVector({self.x}, {self.y})"

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        # BUG: forgot "return self"

bv = BrokenVector(2, 3)
bv *= 2
print(bv)
