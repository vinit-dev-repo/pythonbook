def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Vinit"))                    # fine — positional
print(greet("Vinit", greeting="Hi"))     # fine — greeting is after the /
print(greet(name="Vinit"))               # TypeError — name is positional-only
