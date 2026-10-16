import abc
import collections.abc
from typing import Protocol, runtime_checkable


# 1
class EmailNotifier:
    def send(self, message):
        return f"emailed: {message}"


class SmsNotifier:
    def send(self, message):
        return f"texted: {message}"


def announce(notifier, message):
    print(notifier.send(message))


for notifier in [EmailNotifier(), SmsNotifier()]:
    announce(notifier, "build finished")

# 2
class Basket:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)


print(isinstance(Basket(), collections.abc.Sized))

# 3
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

# 4
class ThirdPartyQueue:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop(0)


class Queue(abc.ABC):
    @abc.abstractmethod
    def push(self, item):
        pass

    @abc.abstractmethod
    def pop(self):
        pass


Queue.register(ThirdPartyQueue)
print(isinstance(ThirdPartyQueue(), Queue))

# 5
@runtime_checkable
class SupportsArea(Protocol):
    def area(self) -> float: ...


print(isinstance(Square(4), SupportsArea))

# 6
print(
    "In these examples, registration or a runtime Protocol match provides "
    "recognition without inheriting methods from that ABC or Protocol."
)
