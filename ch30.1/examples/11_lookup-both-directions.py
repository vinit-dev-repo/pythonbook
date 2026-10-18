try:
    Color["PURPLE"]
except KeyError as e:
    print("by name failed:", e)

try:
    Color(99)
except ValueError as e:
    print("by value failed:", e)
