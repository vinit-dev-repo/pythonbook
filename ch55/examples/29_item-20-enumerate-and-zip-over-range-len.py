fruits = ["apple", "banana", "cherry"]
prices = [1.0, 0.5, 3.0]

# clumsy
for i in range(len(fruits)):
    print(i, fruits[i], prices[i])

# Pythonic
for i, fruit in enumerate(fruits):
    print(i, fruit)

for fruit, price in zip(fruits, prices):
    print(fruit, price)
