from collections import UserDict

class MarkedDict(dict):
    def __getitem__(self, key):
        return "seen:" + super().__getitem__(key)

class MarkedUserDict(UserDict):
    def __getitem__(self, key):
        return "seen:" + super().__getitem__(key)

for kind in (MarkedDict, MarkedUserDict):
    source = kind(status="ready")
    target = {}
    target.update(source)
    print(kind.__name__, source["status"], source.get("status"), target["status"])
