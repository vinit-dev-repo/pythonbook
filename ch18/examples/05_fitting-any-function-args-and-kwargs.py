def loud(func):
    def wrapper(*args, **kwargs):
        print("About to run the function...")
        result = func(*args, **kwargs)
        print("...finished running the function.")
        return result
    return wrapper

@loud
def add(a, b):
    return a + b

print(add(3, 4))
