import copy

original = [[1, 2], [3, 4]]
shallow = original[:]              # slicing makes a shallow copy
deep = copy.deepcopy(original)

original[0][0] = 99
print(shallow)   # inner list is SHARED — it changed too
print(deep)      # deep copy is fully independent
