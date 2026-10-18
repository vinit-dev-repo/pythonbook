# 1
class Letters:
    def __init__(self, text):
        self._text = text

    def __len__(self):
        return len(self._text)

    def __getitem__(self, index):
        return self._text[index]

letters = Letters("hello")
for ch in letters:
    print(ch, end="")
print()
print("h" in letters)
print(list(letters))

# 2
class OnlyLength:
    def __len__(self):
        return 3

only = OnlyLength()
print(len(only))
try:
    only[0]
except TypeError as error:
    print(error)
try:
    for item in only:
        pass
except TypeError as error:
    print(error)

# 3
class Row:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

row = Row("abc")
row[0] = "Z"
del row[1]
print(list(row), len(row))
