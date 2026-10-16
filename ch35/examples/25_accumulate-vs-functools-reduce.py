import itertools
from functools import reduce
import operator

numbers = [1, 2, 3, 4]

print(list(itertools.accumulate(numbers, operator.mul)))  # every running product
print(reduce(operator.mul, numbers))                       # only the final product
