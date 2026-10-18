# 1
registry = {}


def register(cls):
    if cls.__name__ in registry:
        raise ValueError(f"duplicate name: {cls.__name__}")
    registry[cls.__name__] = cls
    return cls


@register
class Cat:
    pass


@register
class Dog:
    pass


print(list(registry))

try:
    @register
    class Cat:
        pass
except ValueError as error:
    print(error)


# 2
def first_instance(cls):
    first = None

    def build(*args, **kwargs):
        nonlocal first
        if first is None:
            first = cls(*args, **kwargs)
        return first

    return build


@first_instance
class Desk:
    def __init__(self, label):
        self.label = label


front = Desk("front")
back = Desk("back")
print(back.label, front is back)

# 3
print(type(Desk).__name__)
try:
    isinstance(front, Desk)
except TypeError as error:
    print(error)
