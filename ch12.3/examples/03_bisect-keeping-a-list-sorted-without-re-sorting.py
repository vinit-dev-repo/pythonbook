import bisect

names = ["Ana", "Carl", "Erin"]
bisect.insort(names, "Ben")
bisect.insort(names, "Dave")
print(names)
