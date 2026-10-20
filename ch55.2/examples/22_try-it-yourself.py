# 1
def log(message, seen=None):
    if seen is None:
        seen = []
    seen.append(message)
    return seen

print(log("a"))
print(log("b"))   # ['b'], not ['a', 'b']


# 2
names = ["Ana", "Ben", "Cy"]
for i, name in enumerate(names):
    print(i, name)
