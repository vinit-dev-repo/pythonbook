# 1
def meow(self):
    return "Meow!"

Cat = type("Cat", (), {"meow": meow})
c = Cat()
print(c.meow())   # Meow!

# 2
class LoggingMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Building {name}")
        return super().__new__(mcs, name, bases, namespace)

class Foo(metaclass=LoggingMeta):
    pass
# prints: Building Foo

# 3
class Base:
    registry = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Base.registry.append(cls.__name__)

class A(Base): pass
class B(Base): pass
print(Base.registry)   # ['A', 'B']

# 4
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

# 5
# a) __init_subclass__ -- validation that runs whenever a subclass is created
# b) class decorator -- one-off change applied to a few unrelated finished classes
# c) __set_name__ -- the descriptor protocol's own hook, made exactly for this
