import sys

# 1
code = hash("hello")
print(isinstance(code, int))
try:
    hash(["h", "e"])
except TypeError as error:
    print("TypeError:", error)

# 2
print(hash((1, 2)) == hash((1, 2)))
try:
    hash((1, [2]))
except TypeError as error:
    print("TypeError:", error)

# 3
low = 17
high = 17 + sys.hash_info.modulus
table = {low: "low", high: "high"}
print(hash(low) == hash(high), low == high)
print(len(table), table[low], table[high])
