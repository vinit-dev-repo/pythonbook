@repeat
def mistaken_greet(name):
    print(f"Hello, {name}!")

returned = mistaken_greet("Ana")
print(callable(returned))
try:
    returned()
except TypeError:
    print("TypeError: the repetition count is a function")
