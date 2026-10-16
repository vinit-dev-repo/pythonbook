class BrokenBox:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return BrokenBox(self.value + other)

    def __radd__(self, other):
        return BrokenBox(other + self.value)

bad = BrokenBox(2) + BrokenBox(3)
print(type(bad.value).__name__, bad.value.value)

class NumberBox:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if type(self) is not NumberBox or type(other) is not NumberBox:
            return NotImplemented
        return NumberBox(self.value + other.value)

left = NumberBox(2)
right = NumberBox(3)
good = left + right
print(type(good).__name__, good.value)
print(left.value, right.value)
