from operator import attrgetter, itemgetter, methodcaller


class PersonTool:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def welcome(self, prefix: str, *, punctuation: str = "!") -> str:
        return f"{prefix}, {self.name}{punctuation}"


person = PersonTool("Ben", 25)
bound = attrgetter("welcome")(person)
print(bound("Hello", punctuation="."))
print(methodcaller("welcome", "Hello", punctuation=".")(person))
try:
    print(attrgetter("missing")(person))
except AttributeError as error:
    print("Missing attribute:", error)
    print("Repair:", getattr(person, "name"))
try:
    print(methodcaller("welcome")(person))
except TypeError as error:
    print("Missing method argument:", error)
    print("Repair:", methodcaller("welcome", "Hello")(person))
try:
    print(itemgetter("age")(person))
except TypeError as error:
    print("PersonTool is not indexable:", error)
