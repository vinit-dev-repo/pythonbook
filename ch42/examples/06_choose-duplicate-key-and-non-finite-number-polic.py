import json
import math

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate object name")
        result[key] = value
    return result

def reject_constant(token):
    raise ValueError("non-finite number token")

def finite_float(token):
    value = float(token)
    if not math.isfinite(value):
        raise ValueError("number exceeds finite float range")
    return value

def load_unique_json(text):
    return json.loads(text, object_pairs_hook=unique_object,
                      parse_constant=reject_constant, parse_float=finite_float)

encoded = json.dumps({1: "numeric key", "1": "text key"})
print(encoded)
print(json.loads(encoded))
for text in [encoded, '{"nested": {"x": 1, "x": 2}}', 'NaN', '1e999']:
    try:
        load_unique_json(text)
    except ValueError:
        print("rejected")
print(load_unique_json('{"values": [1, 2.5, null]}'))
try:
    json.dumps({"value": float("inf")}, allow_nan=False)
except ValueError:
    print("non-finite output refused")
