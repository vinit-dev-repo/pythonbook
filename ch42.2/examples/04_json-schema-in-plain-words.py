from jsonschema import validate, ValidationError

person_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name", "age"],
}

good_data = {"name": "Amy", "age": 28}
bad_data = {"name": "Amy", "age": "twenty-eight"}   # age should be a number

validate(instance=good_data, schema=person_schema)
print("good_data passed")

try:
    validate(instance=bad_data, schema=person_schema)
except ValidationError as e:
    print("bad_data rejected:", e.message)
