people = [("London", "Amy"), ("Paris", "Leo"), ("London", "Sam")]

by_city = defaultdict(list)
for city, name in people:
    by_city[city].append(name)

print(dict(by_city))
