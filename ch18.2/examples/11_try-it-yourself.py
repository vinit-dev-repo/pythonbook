import functools
import time

# 1
def counted(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@counted
def add(a, b):
    return a + b

add(1, 2)
add(3, 4)
print(add.calls)                      # 2

# 2
def tag_a(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("enter a")
        result = func(*args, **kwargs)
        print("leave a")
        return result
    return wrapper

def tag_b(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("enter b")
        result = func(*args, **kwargs)
        print("leave b")
        return result
    return wrapper

@tag_a
@tag_b
def work():
    print("work")

work()                                # enter a, enter b, work, leave b, leave a

# 3
@functools.lru_cache(maxsize=None)
def slow_double(n):
    time.sleep(0.1)
    return n * 2

start = time.perf_counter()
slow_double(4)
print(f"First call:  {time.perf_counter() - start:.2f}s")    # about 0.10s
start = time.perf_counter()
slow_double(4)
print(f"Second call: {time.perf_counter() - start:.2f}s")    # about 0.00s

slow_double.cache_clear()
print(slow_double(4), slow_double(4))                        # 8 8
print(slow_double.cache_info())       # CacheInfo(hits=1, misses=1, maxsize=None, currsize=1)
