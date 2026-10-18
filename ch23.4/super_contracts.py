# super_contracts.py
class NameRoot:
    def __init__(self, label):
        self.label = label

class NamePart(NameRoot):
    def __init__(self, label):
        super().__init__(label)

class CountPart(NameRoot):
    def __init__(self, *, label, count):
        self.count = count
        super().__init__(label)

class BrokenParts(NamePart, CountPart):
    pass

print(NamePart("solo").label)
try:
    BrokenParts("joined")
except TypeError:
    print("sibling signature mismatch")

class NameOption:
    def __init__(self, *, label, **remaining):
        self.label = label
        super().__init__(**remaining)

class CountOption:
    def __init__(self, *, count=0, **remaining):
        self.count = count
        super().__init__(**remaining)

class Configured(NameOption, CountOption):
    pass

configured = Configured(label="joined", count=5)
print(configured.label, configured.count)
try:
    Configured(label="joined", unknown=True)
except TypeError:
    print("unused option rejected")

class IndexBase:
    def __getitem__(self, index):
        return index * 3

class IndexChild(IndexBase):
    def __getitem__(self, index):
        return super().__getitem__(index) + 1

    def proxy_index(self, index):
        return super()[index]

print(IndexChild()[2])
try:
    IndexChild().proxy_index(2)
except TypeError:
    print("super proxy is not subscriptable")
