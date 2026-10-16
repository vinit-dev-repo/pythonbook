import json
from datetime import date

def encode_unknown(obj):
    if isinstance(obj, date):
        return obj.isoformat()      # e.g. "2000-05-01"
    raise TypeError(f"Cannot serialize {type(obj)}")

data = {"birthday": date(2000, 5, 1)}
text = json.dumps(data, default=encode_unknown)
print(text)
