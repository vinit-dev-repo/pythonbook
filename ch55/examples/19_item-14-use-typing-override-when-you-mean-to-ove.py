from typing import override

class Animal:
    def make_sound(self):
        return "..."

class Dog(Animal):
    @override
    def make_sound(self):     # correctly overrides — a method of this name exists on Animal
        return "Woof"

print(Dog().make_sound())
