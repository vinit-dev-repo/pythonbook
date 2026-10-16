common = [1]
original = {"left": common, "right": common}
shallow = original.copy()
deep = copy.deepcopy(original)
print(shallow["left"] is original["left"])
print(deep["left"] is original["left"])
print(deep["left"] is deep["right"])
deep["left"].append(2)
print(original)
print(deep)
