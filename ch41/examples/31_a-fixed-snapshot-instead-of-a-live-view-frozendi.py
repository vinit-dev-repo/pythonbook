from types import MappingProxyType

real = {"a": 1}
view = MappingProxyType(real)
snapshot = frozendict(real)
real["b"] = 2
print(dict(view), dict(snapshot))
print(hash(snapshot) == hash(frozendict(a=1)))
try:
    hash(view)
except TypeError as error:
    print("TypeError:", error)
