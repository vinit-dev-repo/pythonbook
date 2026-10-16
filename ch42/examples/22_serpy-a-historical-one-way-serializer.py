# Optional: python -m pip install serpy==0.3.1
import serpy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonSerializer(serpy.Serializer):
    name = serpy.StrField()
    age = serpy.IntField()

p = Person("Amy", 28)
print(PersonSerializer(p).data)   # object -> dict; field conversion, no incoming-data load API
