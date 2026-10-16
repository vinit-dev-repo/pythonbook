import json
from datetime import date

def decode_person(d):
    if d.get("__type__") == "Person":
        return Person(d["name"], date.fromisoformat(d["birthdate"]))
    return d   # not our marker — leave it as a plain dict

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def __repr__(self):
        return f"Person({self.name!r}, {self.birthdate})"

text = '{"__type__": "Person", "name": "Amy", "birthdate": "2000-05-01"}'
restored = json.loads(text, object_hook=decode_person)
print(restored)
print(type(restored))
