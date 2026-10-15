# import_measure/check.py
import math
from math import sqrt
from timeit import repeat

def qualified():
    return math.sqrt(81)

def direct():
    return sqrt(81)

def local_import():
    from math import sqrt
    return sqrt(81)

print("same result:", qualified() == direct() == local_import() == 9.0)
for function in (qualified, direct, local_import):
    samples = repeat(function, number=20000, repeat=5)
    print(function.__name__, "seconds per 20000 calls:", samples)
