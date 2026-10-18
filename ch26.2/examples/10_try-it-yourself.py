import abc
import collections.abc


# 1
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def summary(self):
        return f"area={self.area()}, perimeter={self.perimeter()}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


print(Square(3).summary())

try:
    Shape()
except TypeError as e:
    print("Failed as expected:", e)

# 2
print(sorted(collections.abc.Sequence.__abstractmethods__))
print(sorted(collections.abc.MutableSequence.__abstractmethods__))


# 3
class Report(abc.ABC):
    @abc.abstractmethod
    def title(self):
        return "report"


class SalesReport(Report):
    def title(self):
        return super().title() + "-sales"


try:
    Report()
except TypeError:
    print("Report cannot be built")
print(SalesReport().title())
