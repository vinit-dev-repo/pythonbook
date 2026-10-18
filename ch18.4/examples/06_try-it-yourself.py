from functools import singledispatch

# 1
def describe_int(x):
    print(f"{x} is a whole number")

def describe_str(x):
    print(f"'{x}' is text, {len(x)} characters")

def describe_default(x):
    print(f"{x} is a {type(x).__name__}")

registry = {int: describe_int, str: describe_str}

def describe(x):
    registry.get(type(x), describe_default)(x)

describe(5)                           # 5 is a whole number
describe("hi")                        # 'hi' is text, 2 characters
describe(2.5)                         # 2.5 is a float

# 2
@singledispatch
def describe(x):
    print(f"{x} is a {type(x).__name__}")

@describe.register
def _(x: int):
    print(f"{x} is a whole number")

describe(True)                        # True is a whole number

# 3
@describe.register
def _(x: bool):
    print(f"{x} is a Boolean")

describe(True)                        # True is a Boolean
describe(5)                           # 5 is a whole number
