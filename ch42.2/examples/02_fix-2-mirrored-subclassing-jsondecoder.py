import json
from datetime import date

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def __repr__(self):
        return f"Person({self.name!r}, {self.birthdate})"

def decode_person(d):
    if d.get("__type__") == "Person":
        return Person(d["name"], date.fromisoformat(d["birthdate"]))
    return d

class MyDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("object_hook", decode_person)
        super().__init__(*args, **kwargs)

text = '{"__type__": "Person", "name": "Amy", "birthdate": "2000-05-01"}'
restored = json.loads(text, cls=MyDecoder)
print(restored)
print(type(restored))
