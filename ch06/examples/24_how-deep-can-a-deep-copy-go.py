import copy

original = [[[4]]]
duplicate = copy.deepcopy(original)
duplicate[0][0].append(9)
print(original)
print(duplicate)
