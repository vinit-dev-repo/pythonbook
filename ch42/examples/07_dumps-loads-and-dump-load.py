import json

person = {"name": "Amy", "age": 28}

text = json.dumps(person)         # dict -> JSON string
print(text)

back = json.loads(text)           # JSON string -> dict
print(back)
