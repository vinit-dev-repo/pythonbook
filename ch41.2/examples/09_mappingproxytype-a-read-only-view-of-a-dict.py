from types import MappingProxyType

real = {"a": 1, "b": 2}
view = MappingProxyType(real)

print(view["a"])       # reading works fine

real["c"] = 3           # change the REAL dict
print(view)              # the view updates too — it's not a copy

try:
    view["d"] = 4        # writing through the view is refused
except TypeError as e:
    print("Error:", e)
