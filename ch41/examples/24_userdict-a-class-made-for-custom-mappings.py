from collections import UserDict

class GoodLowerDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

d = GoodLowerDict()
d["Name"] = "Amy"
d.update({"CITY": "Paris"})   # now goes through YOUR __setitem__ too
print(d)
