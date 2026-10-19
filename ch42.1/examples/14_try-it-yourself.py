import json
import pickle
from datetime import datetime

# 1
data = {"city": "Paris", "visited": True}
raw = pickle.dumps(data)
print(pickle.loads(raw))

# 2
print(json.dumps(data, indent=2))

# 3
def encode_unknown(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Cannot serialize {type(obj)}")


try:
    json.dumps({"when": datetime(2024, 5, 1, 9, 30)})
except TypeError as error:
    print("TypeError:", error)
print(json.dumps({"when": datetime(2024, 5, 1, 9, 30)}, default=encode_unknown))

# 4
trip = {"stops": ("Paris", "Rome"), 1: "first"}
back = json.loads(json.dumps(trip))
print(back)
print(type(back["stops"]).__name__, list(back))
print(pickle.loads(pickle.dumps(trip)) == trip)
