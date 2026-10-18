# 1
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
print(letters[1:3])
print(letters[1])

# 2
a = [1, 2, 3]
b = a
a += [4]
print(b)
c = [1, 2, 3]
d = c
c = c + [4]
print(d)

# 3
letters = ["a", "b", "c", "d", "e"]
letters[1:3] = ["X", "Y", "Z"]
print(letters)

# 4
word = ["a", "b", "c", "d", "e"]
print(word[1:4], word[3:1], word[-2:])
print(len(word[1:4]), word[:2] + word[2:] == word)
