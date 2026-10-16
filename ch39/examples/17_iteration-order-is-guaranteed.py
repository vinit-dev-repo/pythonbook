labels = {1: "integer"}
labels[True] = "boolean"
labels[1.0] = "float"
print(len(labels), labels[1], labels[True], labels[1.0])
