class NamesBox:
    def __init__(self, names):
        self._names = list(names)

    def __iter__(self):
        return iter(self._names)      # delegate: let list's own iterator do the work

for name in NamesBox(["Amy", "Ben"]):
    print(name)
