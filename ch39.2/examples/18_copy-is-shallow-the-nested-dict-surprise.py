import copy

original = {"fruit": ["apple", "banana"]}
deep = copy.deepcopy(original)

deep["fruit"].append("cherry")
print(original)   # untouched
print(deep)
