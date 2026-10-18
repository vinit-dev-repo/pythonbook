import random

random.seed(0)          # fixes the "randomness" so this example is repeatable

items = ["a", "b", "c", "d", "e"]
shuffled = sorted(items, key=lambda x: random.random())
print(shuffled)
