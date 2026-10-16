# 1
import sys
print(sys.version_info)
# Compare the relevant fields with the feature requirement; removed APIs need separate checks.
# if minor >= 10, you have match/case, better errors, X | Y hints
# if minor >= 11, you also have ExceptionGroup / except* and TaskGroup
# if minor >= 12, you also have the nicer f-strings and the shorter generic syntax
# if minor >= 15, you also have lazy import, frozendict and * in comprehensions
# The improved REPL also depends on terminal/platform support.
# The free-threaded build and time-zone data need separate checks.

# 2
price = 4.5
quantity = 3
print(f"Total: {price * quantity}")

# 3
name = "Python"
if (length := len(name)) > 3:
    print(length)   # 6

# 4
def traffic_light(colour):
    match colour:
        case "red":
            return "Stop"
        case "amber":
            return "Wait"
        case "green":
            return "Go"
        case _:
            return "Unknown"

print(traffic_light("green"))   # Go

# 5
a = {"a": 1, "b": 2}
b = {"b": 20, "c": 3}
print(a | b)   # {'a': 1, 'b': 20, 'c': 3}  -- the RIGHT side wins on a clash
