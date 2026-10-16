import random

rng = random.Random(7)
tickets = ["red", "red", "blue"]
print(sorted(rng.sample(tickets, k=3)))
print(rng.choices(["red", "green"], weights=[0, 1], k=4))

cards = ["A", "K", "Q"]
result = rng.shuffle(cards)
print(result is None)
print(sorted(cards))
