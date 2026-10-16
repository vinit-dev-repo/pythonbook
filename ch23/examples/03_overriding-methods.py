class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

print(Dog("Rex").speak())
print(Cat("Tom").speak())
