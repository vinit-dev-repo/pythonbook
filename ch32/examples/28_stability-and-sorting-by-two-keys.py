people = [
    {"name": "Zoe", "age": 30},
    {"name": "Amir", "age": 25},
    {"name": "Bo", "age": 30},
    {"name": "Cass", "age": 25},
]

# Sort by name first (the tie-breaker), THEN by age (the main key).
step1 = sorted(people, key=lambda p: p["name"])
step2 = sorted(step1, key=lambda p: p["age"])

for p in step2:
    print(p["age"], p["name"])
