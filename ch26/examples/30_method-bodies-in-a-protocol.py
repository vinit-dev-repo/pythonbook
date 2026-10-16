from typing import Protocol

class Greeter(Protocol):
    def name(self) -> str: ...

    def greet(self) -> str:          # a Protocol may carry a real method body
        return f"Hello, {self.name()}!"

class Person(Greeter):               # explicitly subclassing it DOES inherit that body
    def name(self) -> str:
        return "Ana"

class Duck:                          # supplies name only; not a full Greeter match
    def name(self) -> str:
        return "Duck"

print(Person().greet())
print(hasattr(Duck(), "greet"))
