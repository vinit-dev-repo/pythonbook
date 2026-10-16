# 1
ages = {"amara": 21, "ravi": 24}
ages["sam"] = 19
print(ages)

# 2
print(ages.get("lee", "unknown"))

# 3
counts = {}
for letter in "mississippi":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)

# 4
red_team = {"amara", "ravi", "sam"}
blue_team = {"sam", "lee"}
print(sorted(red_team & blue_team))      # on both teams
print(sorted(red_team ^ blue_team))      # on exactly one team

# 5
prices = {"apple": 0.5, "bread": 2.2, "milk": 1.1}
for item, price in prices.items():
    if price > 1.0:
        print(item, price)
