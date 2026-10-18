class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"I am {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)          # let Animal set up 'name'
        self.breed = breed

    def describe(self):
        base_text = super().describe()   # get Animal's version first
        return f"{base_text}, a {self.breed}"

d = Dog("Rex", "Labrador")
print(d.describe())
