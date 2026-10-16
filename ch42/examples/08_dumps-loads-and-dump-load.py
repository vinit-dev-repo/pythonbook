import json

person = {"name": "Amy", "age": 28}

with open("person.json", "w", encoding="utf-8") as f:     # plain TEXT mode, not binary
    json.dump(person, f)

with open("person.json", encoding="utf-8") as f:
    back = json.load(f)

print(back)
