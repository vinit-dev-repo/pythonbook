class Creature:
    pass

class Mammal(Creature):
    pass

class Otter(Mammal):
    pass

class Bird(Creature):
    pass

animal = Otter()
print(type(animal) is Otter)
print(type(animal) is Creature)
print(isinstance(animal, Creature))
print(issubclass(Otter, Creature))
print(issubclass(Otter, Bird))
try:
    print(issubclass(animal, Creature))
except TypeError:
    print("TypeError: issubclass needs a class as its first argument")
