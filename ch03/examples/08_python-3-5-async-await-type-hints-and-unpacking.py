defaults = {"colour": "blue", "size": "M"}
overrides = {"size": "L"}
print({**defaults, **overrides})

head = [0, 1]
print([*head, *range(2, 5), *"xy"])

def order(colour, size):
    return f"a {size} {colour} shirt"

print(order(**{**defaults, **overrides}))
