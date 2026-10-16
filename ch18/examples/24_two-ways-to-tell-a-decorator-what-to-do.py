import inspect

def validated(func):
    signature = inspect.signature(func)
    @functools.wraps(func)
    def wrapper(*a, **kw):
        hints = func.__annotations__
        arguments = signature.bind(*a, **kw).arguments
        for name, value in arguments.items():
            want = hints.get(name)
            if want and not isinstance(value, want):
                raise TypeError(f"{name} must be {want.__name__}, got {type(value).__name__}")
        return func(*a, **kw)
    return wrapper

@validated
def greet(name: str, times: int):
    return (name + " ") * times

print(greet("hi", 2))

try:
    greet("hi", "2")
except TypeError as e:
    print("TypeError:", e)
