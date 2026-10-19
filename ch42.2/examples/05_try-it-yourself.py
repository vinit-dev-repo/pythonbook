import json
from datetime import date

from jsonschema import ValidationError, validate


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


# 1
def encode_person(obj):
    if isinstance(obj, Person):
        return {"__type__": "Person", "name": obj.name, "birthdate": obj.birthdate.isoformat()}
    raise TypeError(f"Cannot serialize {type(obj)}")


def decode_person(d):
    if d.get("__type__") == "Person":
        return Person(d["name"], date.fromisoformat(d["birthdate"]))
    return d


original = Person("Ben", date(1999, 12, 31))
text = json.dumps(original, default=encode_person)
restored = json.loads(text, object_hook=decode_person)
print(text)
print(restored.name, restored.birthdate, restored is original)

# 2
book_schema = {
    "type": "object",
    "properties": {"title": {"type": "string"}, "pages": {"type": "integer"}},
    "required": ["title"],
}
validate(instance={"title": "Dune"}, schema=book_schema)
print("Dune passed")
try:
    validate(instance={"pages": 500}, schema=book_schema)
except ValidationError as error:
    print("rejected:", error.message)


# 3
def check(template, data, path="root"):
    if type(data) is not dict:
        return False, f"{path}: not a dictionary"
    if set(template) != set(data):
        return False, f"{path}: keys differ"
    for key, declared in template.items():
        if type(declared) is dict:
            ok, message = check(declared, data[key], f"{path}.{key}")
            if not ok:
                return False, message
        elif type(data[key]) is not declared:
            return False, f"{path}.{key}: wrong type"
    return True, "ok"


template = {"id": str, "place": {"row": int, "column": int}}
print(check(template, {"id": "a1", "place": {"row": 1, "column": 2}}))
print(check(template, {"id": "a1", "place": {"row": 1, "column": "2"}}))
print(check(template, {"id": "a1"}))
