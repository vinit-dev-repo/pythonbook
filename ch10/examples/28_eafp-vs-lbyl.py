prices = {"milk": 1.50}

# LBYL — check first
if "bread" in prices:
    print(prices["bread"])
else:
    print("No price for bread")

# EAFP — just try it
try:
    print(prices["bread"])
except KeyError:
    print("No price for bread")
