import inspect

def counter():
    yield 1
    yield 2

gen = counter()
print(inspect.getgeneratorstate(gen))   # not started yet
next(gen)
print(inspect.getgeneratorstate(gen))   # paused at a yield
