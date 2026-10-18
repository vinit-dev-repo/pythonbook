class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Meta.__new__: creating class '{name}'")
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class Dog(metaclass=Meta):
    def bark(self):
        return "Woof!"

d = Dog()
print(d.bark())
