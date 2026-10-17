import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(99)
print(original)
print(deep)
