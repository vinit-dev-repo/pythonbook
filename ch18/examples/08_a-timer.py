import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        # Elapsed time varies with scheduling and the work being measured.
        print(f"{func.__name__} took {end - start:.3f} seconds")
        return result
    return wrapper
