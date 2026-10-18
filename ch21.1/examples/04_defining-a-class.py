dog = Dog()
dog.name = "Milo"
print(dog.name)
try:
    print(dog.age)
except AttributeError as error:
    print(type(error).__name__)
