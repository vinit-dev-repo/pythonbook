# 1
counts = {}
for letter in "mississippi":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)

# 2
prices = {"apple": 0.5, "bread": 2.2, "milk": 1.1}
for item, price in prices.items():
    if price > 1.0:
        print(item, price)

# 3
students = {"amara": {"age": 21, "course": "Python"}, "ravi": {"age": 24, "course": "Data Science"}}
print(students["ravi"]["course"])      # Data Science
