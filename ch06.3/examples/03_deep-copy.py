import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0].append(99)
print(original)
print(shallow)
