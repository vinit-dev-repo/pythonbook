from typing import Protocol

class Greeter(Protocol):
    def name(self) -> str: ...

    def greet(self) -> str:
        return f"Hello, {self.name()}!"

class Person(Greeter):
    def name(self) -> str:
        return "Ana"

class Duck:
    def name(self) -> str:
        return "Duck"

class Robot:
    def name(self) -> str:
        return "R2"

    def greet(self) -> str:
        return "Beep, R2!"

def announce(greeter: Greeter) -> str:
    return greeter.greet()

print(Person().greet())
print(hasattr(Duck(), "greet"))
print(announce(Robot()))
