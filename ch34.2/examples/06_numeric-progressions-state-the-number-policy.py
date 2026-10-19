from decimal import Decimal
from fractions import Fraction
from itertools import islice
import math


def progression(start, step, stop=None):
    values = (start, step) if stop is None else (start, step, stop)
    supported = (int, float, Fraction, Decimal)
    if any(type(value) not in supported for value in values):
        raise TypeError("use int, float, Fraction or Decimal values")
    other_types = {type(value) for value in values if type(value) is not int}
    if len(other_types) > 1:
        raise TypeError("do not mix distinct non-integer number types")

    def finite(value):
        if type(value) is float:
            return math.isfinite(value)
        if type(value) is Decimal:
            return value.is_finite()
        return True

    if not all(finite(value) for value in values):
        raise ValueError("inputs must be finite")
    if step <= 0:
        raise ValueError("step must be positive")
    number_type = next(iter(other_types), int)
    start, step = number_type(start), number_type(step)
    if stop is not None:
        stop = number_type(stop)
    index, previous = 0, None
    while True:
        value = start + index * step
        if not finite(value):
            raise ArithmeticError("progression overflowed")
        if stop is not None and value >= stop:
            return
        if previous is not None and value <= previous:
            raise ArithmeticError("numeric precision stopped forward progress")
        yield value
        previous = value
        index += 1


class Progression:
    def __init__(self, start, step, stop=None):
        self._arguments = start, step, stop

    def __iter__(self):
        return progression(*self._arguments)


print("integers:", list(progression(2, 3, 11)))
print("floats:", list(progression(1, 0.5, 3)))
print("fractions:", [str(x) for x in progression(0, Fraction(1, 4), 1)])
print("decimals:", [str(x) for x in progression(Decimal("0"), Decimal("0.2"), Decimal("0.6"))])
print("bounded read:", list(islice(progression(4, 2), 3)))
saved = Progression(2, 3, 11)
print("repeat:", list(saved), list(saved))
