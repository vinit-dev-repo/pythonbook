amy = {"apple", "banana", "cherry"}
ben = {"banana", "pear", "grape"}

print("apple" in amy)                   # membership
print(sorted(amy.union(ben)))           # union
print(sorted(amy.intersection(ben)))    # intersection
print(sorted(amy.difference(ben)))      # difference
print({"banana"}.issubset(amy))         # subset
