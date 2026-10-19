# person_boundary.py
import json
from datetime import date

from jsonschema import ValidationError, validate


PERSON_SCHEMA = {
    "type": "object",
    "properties": {
        "__type__": {"const": "Person"},
        "name": {"type": "string", "minLength": 1, "maxLength": 80},
        "birthdate": {"type": "string", "minLength": 10, "maxLength": 10},
    },
    "required": ["__type__", "name", "birthdate"],
    "additionalProperties": False,
}


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __repr__(self):
        return f"Person({self.name!r}, {self.birthdate})"


def load_person(text):
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if len(text) > 4096:
        raise ValueError("text exceeds 4096 characters")
    data = json.loads(text)
    validate(instance=data, schema=PERSON_SCHEMA)
    if data["name"].isspace():
        raise ValueError("name must not be whitespace only")
    birthday = date.fromisoformat(data["birthdate"])
    if birthday.isoformat() != data["birthdate"]:
        raise ValueError("birthdate must use YYYY-MM-DD")
    return Person(data["name"], birthday)


if __name__ == "__main__":
    original = Person("Amy", date(2000, 5, 1))
    restored = load_person('{"__type__": "Person", "name": "Amy", "birthdate": "2000-05-01"}')
    print(type(restored).__name__, restored.name, restored.birthdate)
    print(restored is not original and restored.name == original.name and restored.birthdate == original.birthdate)
