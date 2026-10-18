import functools

# 1
def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper() + "!"
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("Ana"))                   # HELLO ANA!

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

print(add(2, 3))                      # Running...  then  5
print(add.__name__)                   # add

# 3
def twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@twice
def say(text):
    print(text)
    return len(text)

print(say("hi"))                      # hi, hi, then 2

# 4
def bare(func):
    def wrapper():
        return func()
    return wrapper

@bare
def add_pair(a, b):
    return a + b

try:
    add_pair(2, 3)
except TypeError as error:
    print("TypeError:", error)        # wrapper() takes 0 positional arguments but 2 were given
