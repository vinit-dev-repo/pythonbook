def describe_int(x):
    print(f"{x} is a whole number")

def describe_str(x):
    print(f"'{x}' is text, {len(x)} characters")

def describe_default(x):
    print(f"{x} is a {type(x).__name__}")

registry = {
    int: describe_int,
    str: describe_str,
}

def describe(x):
    handler = registry.get(type(x), describe_default)
    handler(x)

describe(5)
describe("hi")
describe(3.14)
