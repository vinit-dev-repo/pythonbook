import itertools

names = ["Ann", "Bo", "Cy"]
for number, name in zip(itertools.count(1), names):
    print(number, name)
