import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

    def reset(self):
        self.calls = 0

@CountCalls
def total(price, *, tax):
    "Return a price after tax."
    return price + tax

@CountCalls
def welcome(name):
    return f"Hello, {name}"

@CountCalls
def reject():
    raise ValueError("not available")

print(total(10, tax=2))
print(welcome("Ana"))
try:
    reject()
except ValueError as error:
    print(type(error).__name__, str(error))
print(total.calls, welcome.calls, reject.calls)
print(total.__name__)
print(total.__doc__)
print(total.__wrapped__.__name__)
total.reset()
print(total.calls)
