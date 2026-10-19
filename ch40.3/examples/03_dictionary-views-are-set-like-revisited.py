required = {"name": str, "age": int, "email": str}
supplied = {"name": "Amy", "age": 30}

missing_keys = required.keys() - supplied.keys()
shared_keys = required.keys() & supplied.keys()

print("Missing:", sorted(missing_keys))
print("Present:", sorted(shared_keys))
