from abc import ABC, abstractmethod

# 1
class Engine:
    def start(self):
        return "Engine started"

class ElectricMotor:
    def start(self):
        return "Motor humming"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

print(Car(Engine()).start())                   # Engine started
print(Car(ElectricMotor()).start())            # Motor humming

# 2
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

try:
    Shape()
except TypeError as error:
    print(type(error).__name__)                # TypeError
print(Square(4).area())                        # 16

# 3
class Duck:
    def move(self):
        return "swims"

class Boat:
    def move(self):
        return "sails"

moves = [thing.move() for thing in [Duck(), Boat()]]
print(moves)                                   # ['swims', 'sails']

# 4
class Account:
    def __init__(self, pin):
        self.__pin = pin

account = Account("1234")
try:
    print(account.__pin)
except AttributeError as error:
    print(type(error).__name__)                # AttributeError
print(account._Account__pin)                   # 1234
