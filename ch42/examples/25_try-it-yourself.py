# 1
import pickle
data = {"city": "Paris", "visited": True}
raw = pickle.dumps(data)
print(pickle.loads(raw))    # {'city': 'Paris', 'visited': True}

# 2
import json
data = {"city": "Paris", "visited": True}
print(json.dumps(data, indent=2))

# 3
import json
from datetime import datetime

def encode_unknown(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Cannot serialize {type(obj)}")

print(json.dumps({"when": datetime.now()}, default=encode_unknown))

# 4
from jsonschema import validate, ValidationError

book_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "pages": {"type": "integer"},
    },
    "required": ["title"],
}

validate(instance={"title": "Dune"}, schema=book_schema)
print("Dune passed")

try:
    validate(instance={"pages": 500}, schema=book_schema)
except ValidationError as e:
    print("rejected:", e.message)

# 5
# pickle.loads() can be crafted to execute arbitrary code as it reconstructs
# objects. Ordinary json.loads() parses JSON into Python data; it does not
# interpret the JSON text as arbitrary Python code. An object_hook is separate
# application code and can choose to construct objects.
#
# Parsing alone is not validation or a resource limit. Set appropriate bounds
# before parsing and check the expected shape and domain rules afterwards.
