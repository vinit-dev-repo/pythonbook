required = {"name": str, "age": int, "email": str}
supplied = {"name": "Amy", "age": 30}

missing = required.keys() - supplied.keys()
print(missing)
