# 2
def average(values):
    """Return the mean of a non-empty list of numbers.

    Raises:
        ValueError: if values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


print(average.__doc__.splitlines()[0])
print(average([2, 4, 9]))
try:
    average([])
except ValueError as error:
    print("ValueError:", error)


# 3
FORMATS = {"upper": str.upper, "title": str.title}


def apply_format(name, text):
    try:
        rule = FORMATS[name]
    except KeyError:
        raise ValueError(f"unknown format: {name}") from None
    return rule(text)


print(apply_format("upper", "ana lee"))
print(apply_format("title", "ana lee"))
try:
    apply_format("snake", "ana lee")
except ValueError as error:
    print("ValueError:", error)
