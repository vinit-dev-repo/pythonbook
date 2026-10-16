import json
from datetime import date

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

def encode_person(obj):
    if isinstance(obj, Person):
        return {
            "__type__": "Person",              # the marker
            "name": obj.name,
            "birthdate": obj.birthdate.isoformat(),
        }
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Cannot serialize {type(obj)}")

p = Person("Amy", date(2000, 5, 1))
text = json.dumps(p, default=encode_person)
print(text)
