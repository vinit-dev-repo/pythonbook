from functools import wraps

def coroutine(func):
    """Old-style decorator: primes a generator-coroutine automatically."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)          # prime it immediately
        return gen
    return wrapper

@coroutine
def echo_v2():
    while True:
        received = yield
        print("got:", received)

gen = echo_v2()
gen.send("no manual priming needed now")
