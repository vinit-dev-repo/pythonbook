class LessOnly:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if type(other) is not LessOnly:
            return NotImplemented
        return self.value < other.value

small = LessOnly(1)
large = LessOnly(2)
print(small < large)
print(large > small)
try:
    print(small <= large)
except TypeError:
    print("TypeError: no accepted <= method")

class ReflectedComparison:
    def __lt__(self, other):
        print("left lt declines")
        return NotImplemented

    def __gt__(self, other):
        print("right gt accepts")
        return True

print(ReflectedComparison() < ReflectedComparison())

class IndependentNe:
    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

one = IndependentNe()
two = IndependentNe()
print(one == two, one != two)
