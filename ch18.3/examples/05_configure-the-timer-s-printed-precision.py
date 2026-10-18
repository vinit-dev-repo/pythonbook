from functools import wraps
from time import perf_counter

def timed(*, digits=3):
    if type(digits) is not int or not 0 <= digits <= 6:
        raise ValueError("digits must be an integer from 0 through 6")
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = func(*args, **kwargs)
            elapsed = perf_counter() - start
            print(f"{func.__name__}: {elapsed:.{digits}f}s")
            return result
        return wrapper
    return decorate

@timed(digits=5)
def combine(left, right):
    return left + right

print(combine(8, right=3))
