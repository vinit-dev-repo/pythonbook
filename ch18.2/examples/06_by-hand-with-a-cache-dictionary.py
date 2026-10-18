import time
import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def slow_square(n):
    time.sleep(0.2)
    return n * n

print(slow_square(5))   # first time: waits ~0.2s
print(slow_square(5))   # second time: returns the saved result
