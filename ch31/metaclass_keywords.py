# metaclass_keywords.py
class ConfigurableMeta(type):
    def __new__(mcs, name, bases, namespace, track=False, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        cls._tracked = track
        return cls

class Parent:
    def __init_subclass__(cls, label, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.label = label

class Child(Parent, metaclass=ConfigurableMeta, track=True, label="ready"):
    pass

assert Child._tracked is True
assert Child.label == "ready"
print(Child._tracked)
print(Child.label)

try:
    class Unexpected(Parent, metaclass=ConfigurableMeta, label="checked", unexpected=True):
        pass
except TypeError:
    print("TypeError")
else:
    raise AssertionError("The unused keyword was silently dropped")

class Later(Parent, metaclass=ConfigurableMeta, track=False, label="later"):
    pass

assert Later._tracked is False and Later.label == "later"
assert Child._tracked is True and Child.label == "ready"
