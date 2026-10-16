import numbers
from decimal import Decimal
from fractions import Fraction

print("Integral is Rational:", issubclass(numbers.Integral, numbers.Rational))
print("bool is Integral:", isinstance(True, numbers.Integral))
print("int is Real:", isinstance(3, numbers.Real))
print("Fraction is Real:", isinstance(Fraction(1, 2), numbers.Real))
print("Decimal is Real:", isinstance(Decimal("1.0"), numbers.Real))
