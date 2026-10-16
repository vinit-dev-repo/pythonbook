class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    pass

d = Dog("Rex")
print(d.name)
print(d.speak())
