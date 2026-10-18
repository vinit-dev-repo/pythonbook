from functools import total_ordering

@total_ordering
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        top = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(top, self.denominator * other.denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

# 1
print(Fraction(1, 2) + Fraction(1, 3))                     # 5/6
print([Fraction(1, 2)])                                    # [Fraction(1, 2)]

# 2
print(Fraction(1, 2) == Fraction(2, 4))                    # True
print(Fraction(1, 2) != Fraction(1, 3))                    # True

# 3
fractions = [Fraction(1, 2), Fraction(1, 3), Fraction(3, 4)]
print(sorted(fractions))
# [Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)]
print(Fraction(1, 3) <= Fraction(1, 2))                    # True

# 4
class Packet:
    def __init__(self, text):
        self.text = text

    def __bytes__(self):
        return self.text.encode("utf-8")

data = bytes(Packet("café"))
print(data, len(data))                                     # b'caf\xc3\xa9' 5
