original = {"fruit": ["apple", "banana"]}
shallow = original.copy()

shallow["fruit"].append("cherry")
print(original)   # changed too!
