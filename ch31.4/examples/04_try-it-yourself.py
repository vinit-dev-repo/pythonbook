# 1
REGISTRY = []

def registered(cls):
    REGISTRY.append(cls.__name__)
    return cls

@registered
class First:
    pass

@registered
class Second:
    pass

print(REGISTRY)

# 2
class NeedsName(type):
    def __new__(mcs, name, bases, namespace):
        if "name" not in namespace:
            raise TypeError(f"{name} must define a name")
        return super().__new__(mcs, name, bases, namespace)

class Good(metaclass=NeedsName):
    name = "good"

try:
    class Bad(metaclass=NeedsName):
        pass
except TypeError as error:
    print(error)

# 3
class Origin:
    def label(self):
        return "origin"

class Child(Origin):
    def label(self):
        return super().label() + ":child"

namespace = {key: value for key, value in vars(Child).items()
             if key not in {"__dict__", "__weakref__"}}
Copy = type("Copy", Child.__bases__, namespace)
try:
    Copy().label()
except TypeError:
    print("copied method retains the old defining class")

def add_kind(cls):
    cls.kind = "kept"
    return cls

Child = add_kind(Child)
print(Child().label(), Child.kind)
