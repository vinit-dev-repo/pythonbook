# normalized_mapping_lab.py
from collections import UserDict
from collections.abc import Mapping

def normalized_key(key):
    if type(key) is not str:
        raise TypeError("keys must be built-in strings")
    result = key.strip().casefold()
    if not result:
        raise ValueError("key must contain non-whitespace text")
    return result

class LabelMap(UserDict):
    def __getitem__(self, key):
        return self.data[normalized_key(key)]

    def __setitem__(self, key, value):
        self.data[normalized_key(key)] = value

    def __delitem__(self, key):
        del self.data[normalized_key(key)]

    def __contains__(self, key):
        return normalized_key(key) in self.data

    def __ior__(self, other):
        self.update(other)
        return self

    def __or__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        result = type(self)(self)
        result.update(other)
        return result

    def __ror__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        result = type(self)(other)
        result.update(self)
        return result

labels = LabelMap({"  North ": 2}, SOUTH=3)
labels.update([("NORTH", 5)])
print(dict(labels), labels.get(" north "), "SOUTH" in labels)
print(labels.setdefault(" south ", 99))
alias = labels
labels |= {" WEST ": 8}
print(alias is labels, labels["west"])
print(dict(labels | {" NORTH ": 7}))
print(dict({" NORTH ": 7, "EAST": 1} | labels))
print(labels.pop("south"))
del labels[" WEST "]
print(dict(labels))
try:
    labels[" "] = 20
except ValueError:
    print("empty name refused")
print(labels.get("absent", -1))
