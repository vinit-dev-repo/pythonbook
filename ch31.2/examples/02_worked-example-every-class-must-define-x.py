class RequireGreetMeta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if "greet" not in namespace:
            raise TypeError(f"{name} must define a 'greet' method")
        return cls

class Animal(metaclass=RequireGreetMeta):
    def greet(self):
        return "..."

try:
    class Rock(metaclass=RequireGreetMeta):
        pass   # forgot to define greet
except TypeError as e:
    print(e)
