from functools import partial, Placeholder

at_rate_three = partial(charge, Placeholder, 3)
print(at_rate_three(4))
try:
    at_rate_three()
except TypeError:
    print("a reserved position needs a value")
