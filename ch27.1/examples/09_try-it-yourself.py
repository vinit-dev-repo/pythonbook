from operator import attrgetter, methodcaller


# 1
class Greeter:
    def __call__(self, name):
        return "hello " + name


print(callable(Greeter), callable(Greeter()), callable("text"))
print(Greeter()("Amy"))


# 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"


people = [Person("Amy", 30), Person("Ben", 25), Person("Cal", 35)]
print(sorted(people, key=attrgetter("age")))


# 3
print(list(map(methodcaller("upper"), ["a", "b"])))
