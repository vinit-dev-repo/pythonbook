import itertools

runners = ["Ann", "Bo", "Cy"]
podiums = list(itertools.permutations(runners, 2))
print(podiums)
print(len(podiums))
