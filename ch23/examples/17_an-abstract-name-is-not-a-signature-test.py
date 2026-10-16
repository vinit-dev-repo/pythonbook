from abc import ABC, abstractmethod

class AreaContract(ABC):
    @abstractmethod
    def area(self):
        pass

class WrongSignature(AreaContract):
    def area(self, scale):
        return scale

class NonCallableArea(AreaContract):
    area = 12

wrong = WrongSignature()
noncallable = NonCallableArea()
print(type(wrong).__name__, type(noncallable).__name__)
try:
    wrong.area()
except TypeError:
    print("TypeError: required argument is missing")
try:
    noncallable.area()
except TypeError:
    print("TypeError: area is not callable")
