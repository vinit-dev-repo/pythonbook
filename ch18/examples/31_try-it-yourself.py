# 4: a self-contained value and cache check
import functools
import time

@functools.lru_cache(maxsize=None)
def slow_double(n):
    time.sleep(0.1)
    return n * 2

slow_double.cache_clear()
print(slow_double(4), slow_double(4))
print(slow_double.cache_info())
