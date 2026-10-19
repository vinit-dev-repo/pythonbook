from operator import attrgetter, itemgetter, methodcaller


class PersonTool:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def welcome(self, prefix: str, *, punctuation: str = "!") -> str:
        return f"{prefix}, {self.name}{punctuation}"

    def __repr__(self) -> str:
        return f"PersonTool({self.name!r}, {self.age})"


people = [PersonTool("Ben", 25), PersonTool("Amy", 25), PersonTool("Cal", 30)]
attribute_name = "age"
key = attrgetter(attribute_name, "name")
attribute_name = "name"
print(sorted(people, key=key))
print(key(people[0]))
