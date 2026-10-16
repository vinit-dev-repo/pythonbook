import itertools

flavours = ["vanilla", "chocolate", "strawberry"]
two_scoops = list(itertools.combinations_with_replacement(flavours, 2))
print(two_scoops)
print(len(two_scoops))
