import functools
import time

# 1
def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper() + "!"
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("Ana"))          # HELLO ANA!

# 2
def announce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Running...")
        return func(*args, **kwargs)
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 3))             # Running...  then  5
print(add.__name__)          # add

# 3
def multiply_result(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * n
        return wrapper
    return decorator

@multiply_result(10)
def get_price():
    return 5

print(get_price())           # 50

# 4
@functools.lru_cache(maxsize=None)
def slow_double(n):
    time.sleep(0.1)
    return n * 2

start = time.perf_counter()
slow_double(4)
print(f"First call:  {time.perf_counter() - start:.2f}s")   # ~0.10s

start = time.perf_counter()
slow_double(4)
print(f"Second call: {time.perf_counter() - start:.2f}s")   # ~0.00s
