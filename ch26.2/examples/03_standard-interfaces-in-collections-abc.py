from collections.abc import Sequence


class ReadingList(Sequence):
    def __init__(self, titles):
        self._titles = list(titles)

    def __getitem__(self, index):
        return self._titles[index]

    def __len__(self):
        return len(self._titles)


names = ["Ada", "Lin", "Ada"]
reading = ReadingList(names)
names[0] = "Changed"
print(reading.count("Ada"))
print(reading.index("Ada"))
print(list(reading))
