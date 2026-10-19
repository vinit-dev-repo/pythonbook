# 1
visits = ["home", "about", "home", "contact", "about"]
print(list(dict.fromkeys(visits)))

# 2
roles = frozenset({"admin", "editor"})
descriptions = {roles: "Can manage and publish content"}
print(descriptions[frozenset({"editor", "admin"})])

# 3
required = {"name": str, "age": int, "email": str}
supplied = {"name": "Amy", "age": 30}
print(sorted(required.keys() - supplied.keys()))
print(sorted(required.keys() & supplied.keys()))

# 4
team_a = ["Amy", "Ben", "Cara"]
team_b = ["Ben", "Dan", "Amy"]
print(sorted(set(team_a) & set(team_b)))
print(sorted(set(team_a) - set(team_b)))
print(sorted(set(team_b) - set(team_a)))
