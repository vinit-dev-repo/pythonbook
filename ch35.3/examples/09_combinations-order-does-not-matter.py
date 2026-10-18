import itertools

toppings = ["mushroom", "olive", "pepper", "onion"]
pairs = list(itertools.combinations(toppings, 2))
print(pairs)
print(len(pairs))
