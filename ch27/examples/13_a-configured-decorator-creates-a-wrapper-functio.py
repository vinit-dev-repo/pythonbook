import functools


class LabelCalls:
    def __init__(self, label):
        self.label = label

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"label={self.label}")
            return func(*args, **kwargs)
        return wrapper


def original_blue(name):
    return name.upper()


paint_blue = LabelCalls("blue")(original_blue)


@LabelCalls("green")
def paint_green(name):
    return name.upper()


print(type(paint_blue).__name__)
print(paint_blue("ana"))
print(paint_green("ben"))
print(paint_blue.__wrapped__ is original_blue)
