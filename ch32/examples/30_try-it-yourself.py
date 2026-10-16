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
class Letters:
    def __init__(self, text):
        self._text = text
    def __len__(self):
        return len(self._text)
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Letters(self._text[index])
        return self._text[index]
    def __repr__(self):
        return f"Letters({self._text!r})"

letters = Letters("hello")
print(letters[1:3])   # Letters('el')

# 3
a = [1, 2, 3]
b = a
a += [4]
print(b)   # [1, 2, 3, 4] -- b changed too, same object

# 4
people = [{"name": "A", "score": 5}, {"name": "B", "score": 9}, {"name": "C", "score": 5}]
result = sorted(people, key=lambda p: p["score"], reverse=True)
print(result)
# [{'name': 'B', 'score': 9}, {'name': 'A', 'score': 5}, {'name': 'C', 'score': 5}]

# 5
letters = ["a", "b", "c", "d", "e"]
letters[1:3] = ["X", "Y", "Z"]
print(letters)   # ['a', 'X', 'Y', 'Z', 'd', 'e']
