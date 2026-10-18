import itertools

print("empty:", all([]), any([]), sum([], start=10))
print("defaults:", min([], default="missing"), max([], default="missing"))
values = [0, "", 3, None, "ready"]
print("truthy:", list(filter(None, values)))
print("falsy:", list(itertools.filterfalse(None, values)))

source = iter([0, 4, 9])
print("any:", any(source), "remaining:", list(source))
source = iter([2, 0, 9])
print("all:", all(source), "remaining:", list(source))
print("short mask:", list(itertools.compress(["a", "b", "c"], [1, 0])))
