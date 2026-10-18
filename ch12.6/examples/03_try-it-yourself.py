# 1
import csv
record = next(csv.reader(['~a|b~| x |1'], delimiter='|', quotechar='~', skipinitialspace=True))
print(record)          # ['a|b', 'x ', '1']

# 2
from statistics import NormalDist
print(set(NormalDist(mu=10, sigma=0).samples(8, seed=5)))   # {10.0}

# 3
import random
random.seed(1)
print({random.randrange(3, 5) for _ in range(10)})   # a subset of {3, 4}
