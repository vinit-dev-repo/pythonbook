# namespace_policy.py
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
    class StrictProperty(metaclass=StrictMeta):
        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            self._value = new_value
except TypeError as error:
    print(error)
else:
    raise AssertionError("The strict namespace accepted a repeated value name")

class OrdinaryProperty:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

ordinary = OrdinaryProperty()
ordinary.value = 5
assert ordinary.value == 5
print(ordinary.value)
