import json

data = {"coords": (3, 4), 1: "one"}
text = json.dumps(data)
print(text)

restored = json.loads(text)
print(restored)
print(type(restored["coords"]))
