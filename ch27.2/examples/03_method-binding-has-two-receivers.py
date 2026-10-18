import functools

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

class BrokenLedger:
    def __init__(self):
        self.total = 0

    @CountCalls
    def add(self, amount):
        self.total += amount
        return self.total

try:
    BrokenLedger().add(3)
except TypeError as error:
    print(type(error).__name__)

def count_method(func):
    calls = 0

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        nonlocal calls
        calls += 1
        return func(self, *args, **kwargs)

    def get_calls():
        return calls

    wrapper.get_calls = get_calls
    return wrapper

class Ledger:
    def __init__(self):
        self.total = 0

    @count_method
    def add(self, amount):
        self.total += amount
        return self.total

first = Ledger()
second = Ledger()
print(first.add(3))
print(second.add(7))
print(first.total, second.total)
print(Ledger.add.get_calls())
