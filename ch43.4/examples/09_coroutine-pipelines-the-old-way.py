# --- Shape 1: PULLING data -- a chain of plain generators, pulled with next() ---
def read_numbers():
    for n in [1, 2, 3, 4]:
        yield n

def double_each(source):
    for n in source:
        yield n * 2

pipeline = double_each(read_numbers())
for value in pipeline:
    print("pulled:", value)

# --- Shape 2: PUSHING data -- send() through a chain of coroutines ---
from functools import wraps

def coroutine(func):
    """Same priming decorator as before."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def printer():
    while True:
        line = yield
        print("printed:", line)

@coroutine
def uppercase(target):
    while True:
        line = yield
        target.send(line.upper())   # PUSH the result to the next coroutine

pipeline_in = uppercase(printer())
pipeline_in.send("hello")
pipeline_in.send("world")

# --- Shape 3: BROADCASTING data -- one producer, several consumer coroutines ---
@coroutine
def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)        # PUSH the same item to every consumer

@coroutine
def consumer(name):
    while True:
        item = yield
        print(f"{name} received: {item}")

fanout = broadcast([consumer("A"), consumer("B"), consumer("C")])
fanout.send("news flash")
