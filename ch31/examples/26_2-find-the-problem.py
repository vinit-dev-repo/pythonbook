class Tag:
    def __init__(self, label):
        self.label = label

    def __eq__(self, other):
        return self.label == other.label

a, b = Tag("urgent"), Tag("urgent")
print(a == b)
try:
    print({a, b})
except TypeError as e:
    print("TypeError:", e)
