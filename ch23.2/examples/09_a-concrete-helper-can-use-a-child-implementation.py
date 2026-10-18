from abc import ABC, abstractmethod

class MeasuredShape(ABC):
    @abstractmethod
    def area(self):
        pass

    def report(self):
        return f"Area: {self.area()}"

class MeasuredSquare(MeasuredShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

measured = MeasuredSquare(3)
print(measured.report())
