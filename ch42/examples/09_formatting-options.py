import json

data = {"b": 2, "a": 1, "city": "café"}

print(json.dumps(data, indent=2))                         # human-readable, multi-line
print(json.dumps(data, sort_keys=True))                   # keys always in the same order
print(json.dumps(data, ensure_ascii=False))                # keep real unicode characters
