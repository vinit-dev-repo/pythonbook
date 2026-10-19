from collections import ChainMap, UserDict
from types import MappingProxyType

# 1
user_prefs = {"volume": 90}
defaults = {"volume": 50, "brightness": 70}
settings = ChainMap(user_prefs, defaults)
print(settings["volume"])
print(settings["brightness"])

# 2
settings["brightness"] = 40
print(user_prefs, defaults)
temporary = settings.new_child({"volume": 10})
print(temporary["volume"], settings["volume"])


# 3
class BadLowerDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)


class GoodLowerDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)


bad = BadLowerDict()
bad.update({"CITY": "Paris"})
good = GoodLowerDict()
good.update({"CITY": "Paris"})
good |= {"ZONE": 4}
print(dict(bad))
print(dict(good))

# 4
stock = {"apples": 10}
public_stock = MappingProxyType(stock)
stock["apples"] = 3
print(public_stock["apples"])
try:
    public_stock["apples"] = 99
except TypeError as error:
    print("Blocked:", error)

# 5
source = {"labels": ["new"]}
public = MappingProxyType(source)
public["labels"].append("checked")
print(source["labels"])
snapshot = dict(public)
source["extra"] = 1
print(sorted(snapshot), sorted(public))
