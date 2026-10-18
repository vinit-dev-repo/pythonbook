# 1
class Dog:
    def speak(self):
        return "woof"


print(type(Dog.speak).__name__, type(Dog().speak).__name__)

# 2
dog = Dog()
dog.speak = "quiet"
print(dog.speak)
print(Dog().speak())


# 3
class Celsius:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        instance.__dict__[self.private_name] = value


class Thermometer:
    reading = Celsius()

    def __init__(self, reading):
        self.reading = reading


t = Thermometer(20)
print(t.reading)
try:
    t.reading = -300
except ValueError as error:
    print(error)
print(t.reading)
