import itertools
import operator

daily_growth = [1.1, 1.2, 0.9, 1.05]
running_product = itertools.accumulate(daily_growth, operator.mul)
print([round(x, 3) for x in running_product])
