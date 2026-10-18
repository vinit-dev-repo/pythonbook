class LeftMissing:
    pass

class LeftDeclines:
    def __add__(self, other):
        print("left declines")
        return NotImplemented

class RightAccepts:
    def __radd__(self, other):
        print("right accepts")
        return "result"

class SameDeclines:
    def __add__(self, other):
        print("same forward")
        return NotImplemented

    def __radd__(self, other):
        print("same reflected")
        return "not reached"

print(LeftMissing() + RightAccepts())
print(LeftDeclines() + RightAccepts())
try:
    print(SameDeclines() + SameDeclines())
except TypeError:
    print("TypeError: both operands unsupported")

class DomainFailure:
    def __add__(self, other):
        raise ValueError("invalid supported value")

try:
    print(DomainFailure() + RightAccepts())
except ValueError as error:
    print(error)
print(LeftDeclines.__add__(LeftDeclines(), RightAccepts()) is NotImplemented)
try:
    print(bool(NotImplemented))
except TypeError:
    print("TypeError: NotImplemented has no truth value")
