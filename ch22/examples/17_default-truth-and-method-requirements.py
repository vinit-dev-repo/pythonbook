class Plain:
    pass

class Both:
    def __bool__(self):
        return False

    def __len__(self):
        return 5

class BadTruth:
    def __bool__(self):
        return 0

    def __len__(self):
        return 5

class BadLength:
    def __len__(self):
        return -1

print(bool(Plain()))
print(bool(Both()), len(Both()))
print(BadTruth().__bool__())
try:
    print(bool(BadTruth()))
except TypeError:
    print("TypeError: __bool__ must return bool")
try:
    print(len(BadLength()))
except ValueError:
    print("ValueError: length must be nonnegative")
