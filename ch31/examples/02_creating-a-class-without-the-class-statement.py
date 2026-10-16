def bark(self):
    return f"{self.name} says Woof!"

Dog = type(
    "Dog",                       # name of the new class
    (),                           # tuple of base classes (none here)
    {"bark": bark, "species": "Canine"},   # namespace: attributes + methods
)

d = Dog()
d.name = "Rex"
print(d.bark())
print(Dog.species)
print(type(Dog))
