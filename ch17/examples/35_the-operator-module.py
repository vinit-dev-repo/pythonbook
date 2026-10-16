from operator import itemgetter

people = [("Amy", 30), ("Ben", 25), ("Cal", 35)]
print(sorted(people, key=itemgetter(1)))     # sort by age (index 1)
