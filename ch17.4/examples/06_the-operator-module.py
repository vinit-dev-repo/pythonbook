from functools import reduce
from operator import add, mul

numbers = [1, 2, 3, 4]
print(reduce(add, numbers))
print(reduce(mul, numbers))
