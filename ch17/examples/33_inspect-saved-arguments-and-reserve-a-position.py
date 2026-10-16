from functools import partial

def charge(units, rate):
    return units * rate

standard_charge = partial(charge, rate=3)
print(standard_charge.func is charge)
print(standard_charge.args, standard_charge.keywords)
print(standard_charge(4), standard_charge(4, rate=5))
