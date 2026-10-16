# Optional: python -m pip install marshmallow==4.3.1
from marshmallow import Schema, fields, ValidationError

class PersonSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)

schema = PersonSchema()

good = schema.load({"name": "Amy", "age": 28})    # validates AND loads
print(good)

dumped = schema.dump({"name": "Amy", "age": 28})  # dict -> plain dict, ready for json.dumps
print(dumped)

try:
    schema.load({"name": "Amy", "age": "not a number"})
except ValidationError as e:
    print("rejected:", e.messages)
