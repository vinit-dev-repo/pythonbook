basket.remove("bread")     # crashes if "bread" is not in the set
print(sorted(basket))

basket.discard("eggs")     # does NOT crash if "eggs" is not in the set
print(sorted(basket))
