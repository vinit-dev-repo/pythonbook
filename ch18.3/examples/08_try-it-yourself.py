import functools
import inspect

# 1
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

print(get_price())                    # 50

# 2
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat
def mistaken_greet(name):
    print(f"Hello, {name}!")

returned = mistaken_greet("Ana")
print(callable(returned))             # True
try:
    returned()
except TypeError:
    print("TypeError: the repetition count is a function")

# 3
commands = {}

def command(name):
    def decorate(func):
        commands[name] = func
        return func
    return decorate

@command("status")
def status():
    return "ready"

@command("stop")
def stop():
    return "stopped"

print(sorted(commands))               # ['status', 'stop']
print(commands["stop"]())             # stopped

# 4
def validated(func):
    signature = inspect.signature(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        hints = func.__annotations__
        arguments = signature.bind(*args, **kwargs).arguments
        for name, value in arguments.items():
            want = hints.get(name)
            if want and not isinstance(value, want):
                raise TypeError(f"{name} must be {want.__name__}, got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper

@validated
def area(width: int, height: int):
    return width * height

print(area(2, 3))                     # 6
try:
    area(2, "3")
except TypeError as error:
    print("TypeError:", error)        # height must be int, got str
