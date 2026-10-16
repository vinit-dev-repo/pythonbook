import json
from datetime import date

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def __repr__(self):
        return f"Person({self.name!r}, {self.birthdate})"

def encode_person(obj):
    if isinstance(obj, Person):
        return {"__type__": "Person", "name": obj.name, "birthdate": obj.birthdate.isoformat()}
    raise TypeError(f"Cannot serialize {type(obj)}")

def decode_person(d):
    if d.get("__type__") == "Person":
        return Person(d["name"], date.fromisoformat(d["birthdate"]))
    return d

original = Person("Amy", date(2000, 5, 1))

text = json.dumps(original, default=encode_person)
restored = json.loads(text, object_hook=decode_person)

print(text)
print(restored)
print(restored.name == original.name and restored.birthdate == original.birthdate)
