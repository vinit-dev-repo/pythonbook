def greet(name, greeting="Hello"):
    """Say hello to someone."""
    return f"{greeting}, {name}!"

print(greet.__name__)
print(greet.__doc__)
print(greet.__defaults__)
