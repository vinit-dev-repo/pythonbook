# parameter_rules.py
from functools import wraps
from inspect import signature

def check_parameters(**rules):
    def decorate(func):
        shape = signature(func)
        if rules.keys() - shape.parameters.keys():
            raise ValueError("rule names must be declared parameters")
        if not all(callable(rule) for rule in rules.values()):
            raise TypeError("each rule must be callable")

        @wraps(func)
        def call(*args, **kwargs):
            bound = shape.bind(*args, **kwargs)
            bound.apply_defaults()
            for name, rule in rules.items():
                if not rule(bound.arguments[name]):
                    raise ValueError("rule rejected " + name)
            return func(*args, **kwargs)
        return call
    return decorate

def small_quantity(value):
    return type(value) is int and 1 <= value <= 8

entered = []

@check_parameters(quantity=small_quantity)
@check_parameters(label=lambda value: isinstance(value, str) and bool(value.strip()))
def reserve(quantity=2, *, label="desk"):
    entered.append((quantity, label))
    return quantity, label

print(reserve())
print(reserve(label="window", quantity=4))
for args, kwargs in [((9,), {}), ((), {"label": " "}), ((3,), {"quantity": 4})]:
    try:
        reserve(*args, **kwargs)
    except (TypeError, ValueError) as error:
        print(type(error).__name__)
print(entered)
print(reserve.__name__)
