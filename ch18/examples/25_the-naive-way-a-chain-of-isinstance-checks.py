def describe(x):
    if isinstance(x, int):
        print(f"{x} is a whole number")
    elif isinstance(x, str):
        print(f"'{x}' is text, {len(x)} characters")
    else:
        print(f"{x} is a {type(x).__name__}")
