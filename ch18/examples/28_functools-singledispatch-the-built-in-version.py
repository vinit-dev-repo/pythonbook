from functools import singledispatch

@singledispatch
def describe(x):
    print(f"{x} is a {type(x).__name__}")

@describe.register
def _(x: int):
    print(f"{x} is a whole number")

@describe.register
def _(x: str):
    print(f"'{x}' is text, {len(x)} characters")

describe(5)
describe("hi")
describe(3.14)
