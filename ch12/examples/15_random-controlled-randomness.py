import random

random.seed(12345)        # fixes this sequence for a compatible generator and these calls

print(random.random())
print(random.randint(1, 6))
print(random.choice(["rock", "paper", "scissors"]))
print(random.sample(range(1, 50), k=6))

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print(cards)
