import functools

def loud(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("About to run the function...")
        result = func(*args, **kwargs)
        print("...finished running the function.")
        return result
    return wrapper

@loud
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)
print(add.__doc__)
