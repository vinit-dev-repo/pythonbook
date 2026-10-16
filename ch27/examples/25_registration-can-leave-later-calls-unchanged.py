registry = {}


def register(obj):
    name = obj.__name__
    if name in registry:
        raise ValueError(f"duplicate registration: {name}")
    registry[name] = obj
    return obj


@register
def double(value):
    return value * 2


@register
class Label:
    def __init__(self, text):
        self.text = text


def add_category(cls):
    cls.category = "note"
    return cls


class ManualNote:
    pass


ManualNote = add_category(ManualNote)


@add_category
class DecoratedNote:
    pass


print("registry:", sorted(registry), double(3), Label("ok").text)
print("same registered objects:", registry["double"] is double, registry["Label"] is Label)
print("helper and decoration:", ManualNote.category, DecoratedNote.category)
try:
    register(double)
except ValueError as error:
    print("duplicate rejected:", error)
print("original registration remains:", registry["double"] is double)
