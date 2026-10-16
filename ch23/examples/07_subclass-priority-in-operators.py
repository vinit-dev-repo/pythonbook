class BaseAdd:
    def __add__(self, other):
        print("base add")
        return "base result"

    def __radd__(self, other):
        print("base reflected")
        return "reflected result"

class ChildAdd(BaseAdd):
    def __radd__(self, other):
        print("child reflected")
        return NotImplemented

class InheritedAdd(BaseAdd):
    pass

print(BaseAdd() + ChildAdd())
print(BaseAdd() + InheritedAdd())

class BaseCompare:
    def __lt__(self, other):
        print("base lt")
        return False

    def __gt__(self, other):
        print("right gt")
        return True

class ChildCompare(BaseCompare):
    pass

print(BaseCompare() < ChildCompare())
