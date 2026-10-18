from decimal import Decimal
from timeit import repeat

float_values = [0.25] * 1000
decimal_values = [Decimal("0.25")] * 1000

def float_total():
    return sum(float_values)

def decimal_total():
    return sum(decimal_values, Decimal(0))

print(float_total() == decimal_total() == 250)
for name, operation in (("float", float_total), ("decimal", decimal_total)):
    batches = repeat(operation, number=100, repeat=3)
    print(name, "seconds per call:", min(batches) / 100)
