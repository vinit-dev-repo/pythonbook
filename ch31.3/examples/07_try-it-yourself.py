# 1
class FrozenPoint:
    def __init__(self, x, y):
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)

    def __setattr__(self, name, value):
        raise AttributeError("FrozenPoint cannot be changed after creation")

fp = FrozenPoint(1, 2)
print(fp.x, fp.y)
try:
    fp.x = 99
except AttributeError as e:
    print(e)

# 2
class Labelled(type):
    @property
    def status(cls):
        return cls.__dict__.get("_status", "new")

    def describe(cls):
        return "class " + cls.__name__

class Item(metaclass=Labelled):
    pass

print(Item.status)
print(Item.describe())
try:
    Item().describe()
except AttributeError:
    print("metaclass method absent on instance")

# 3
class Fallback:
    present = "here"

    def __getattr__(self, name):
        return "missing: " + name

obj = Fallback()
print(obj.anything)
print(obj.present)
