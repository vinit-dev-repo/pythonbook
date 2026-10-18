# 1
people = [{"name": "A", "score": 5}, {"name": "B", "score": 9}, {"name": "C", "score": 5}]
result = sorted(people, key=lambda p: p["score"], reverse=True)
print(result)

# 2
print([1, 2] < [1, 2, 0], (2, 0) < (1, 9), [1, 2] == (1, 2))
try:
    print([1, "a"] < [1, 2])
except TypeError as error:
    print("TypeError:", error)

# 3
x = "outside"
doubled = [x * 2 for x in range(3)]
print(doubled, x)

# 4
def unique(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

print(unique("level"))
print(unique([[2], [2], [4]]))
