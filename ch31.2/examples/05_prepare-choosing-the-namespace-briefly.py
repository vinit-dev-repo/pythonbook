class NoDuplicatesDict(dict):
    def __setitem__(self, key, value):
        if key in self and not key.startswith("__"):
            raise TypeError(f"Duplicate attribute: {key}")
        super().__setitem__(key, value)

class StrictMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        return NoDuplicatesDict()

try:
    class Config(metaclass=StrictMeta):
        timeout = 30
        timeout = 60   # oops, redefined by accident
except TypeError as e:
    print(e)
