import functools


# 1
class CallCounter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} time(s)")
        return self.func(*args, **kwargs)


@CallCounter
def wave():
    print("Wave!")


wave()
wave()


# 2
def hello():
    print("hello")


hello = CallCounter(hello)
hello()
print(type(hello).__name__, hello.count)


# 3
class Ledger:
    @CallCounter
    def add(self, amount):
        return amount


try:
    Ledger().add(3)
except TypeError as error:
    print(error)
