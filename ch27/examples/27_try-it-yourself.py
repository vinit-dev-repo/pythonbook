# 3
people = [Person("Amy", 30), Person("Ben", 25), Person("Cal", 35)]
print(sorted(people, key=attrgetter("age")))
