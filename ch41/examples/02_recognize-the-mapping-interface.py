from collections import UserDict
from collections.abc import Mapping, MutableMapping
from types import MappingProxyType

for value in ({"x": 1}, UserDict(x=1), MappingProxyType({"x": 1})):
    print(isinstance(value, Mapping), isinstance(value, MutableMapping))
print(isinstance([("x", 1)], Mapping))
