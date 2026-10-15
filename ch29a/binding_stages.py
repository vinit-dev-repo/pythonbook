# binding_stages.py
from functools import wraps

class BrokenDecorator:
    def __init__(self, func):
        self.func = func

    def __get__(self, subject, owner=None):
        return self

    def __call__(self, amount):
        return self.func(amount)


def broken(func):
    return BrokenDecorator(func)

def repaired(func):
    calls = 0
    @wraps(func)
    def call(subject, *args, **kwargs):
        nonlocal calls
        calls += 1
        return func(subject, *args, **kwargs)

    call.calls = lambda: calls
    return call


class MethodsOnly:
    def __init__(self, func):
        self.func = func

    def __get__(self, subject, owner=None):
        if subject is None:
            return self

        def call(*args, **kwargs):
            return self.func(subject, *args, **kwargs)

        return call


class BrokenInventory:
    def __init__(self, quantity):
        self.quantity = quantity

    @broken
    def add(self, amount):
        self.quantity += amount
        return self.quantity


class RepairedInventory:
    def __init__(self, quantity):
        self.quantity = quantity

    @repaired
    def add(self, amount):
        self.quantity += amount
        return self.quantity


class MethodInventory:
    def __init__(self, quantity):
        self.quantity = quantity

    @MethodsOnly
    def add(self, amount):
        self.quantity += amount
        return self.quantity


@MethodsOnly
def standalone(text):
    return text.upper()

if __name__ == '__main__':
    bad = BrokenInventory(10)
    try:
        bad.add(2)
    except TypeError as error:
        print(type(error).__name__, bad.quantity)

    east = RepairedInventory(10)
    west = RepairedInventory(20)
    print(east.add(2), west.add(3), RepairedInventory.add.calls())
    print(MethodInventory(10).add(2))
    try:
        standalone('west')
    except TypeError as error:
        print(type(error).__name__)
