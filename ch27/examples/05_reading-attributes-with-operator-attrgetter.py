from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"

people_objects = [Person("Amy", 30), Person("Ben", 25)]
print(sorted(people_objects, key=attrgetter("age")))
