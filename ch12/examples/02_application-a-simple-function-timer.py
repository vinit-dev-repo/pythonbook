import time

def time_it(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    # Display elapsed time to tenths by rounding down.
    # Fewer displayed digits do not make the measurement constant.
    print(f"{func.__name__} took {int((end - start) * 10) / 10:.1f} seconds")
    return result

def slow_square(n):
    time.sleep(0.2)
    return n ** 2
