class Countback:
    def __init__(self, values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __reversed__(self):
        return iter(self._values[::-1])

for n in reversed(Countback([1, 2, 3])):
    print(n)
