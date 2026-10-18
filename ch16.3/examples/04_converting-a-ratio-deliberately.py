from fractions import Fraction

numerator, denominator = (0.625).as_integer_ratio()
print(numerator, denominator)
print(Fraction(numerator, denominator))
print(Fraction("0.2") == Fraction(1, 5))
print(Fraction(0.2) == Fraction(1, 5))
print(Fraction(2, 5) + 1)
print(type(Fraction(2, 5) + 1.0).__name__)
