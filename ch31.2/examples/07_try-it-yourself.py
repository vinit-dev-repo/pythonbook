# 1
class LoggingMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Building {name}")
        return super().__new__(mcs, name, bases, namespace)

class Foo(metaclass=LoggingMeta):
    pass
# prints: Building Foo

# 2
class Base:
    registry = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Base.registry.append(cls.__name__)

class A(Base): pass
class B(Base): pass
print(Base.registry)   # ['A', 'B']

# 3
# a) __init_subclass__ -- validation that runs whenever a subclass is created
# b) class decorator -- one-off change applied to a few unrelated finished classes
# c) __set_name__ -- the descriptor protocol's own hook, made exactly for this
