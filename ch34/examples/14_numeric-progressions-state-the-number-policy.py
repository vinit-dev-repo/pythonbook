from fractions import Fraction
from itertools import count, takewhile

values = count(Fraction(1, 4), Fraction(1, 4))
below_one = takewhile(lambda value: value < 1, values)
print([str(value) for value in below_one])
print("next after boundary:", next(values))
