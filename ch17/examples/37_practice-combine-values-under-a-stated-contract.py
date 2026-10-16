def combine_values(first, /, *rest, **named):
    result = first
    for value in (*rest, *named.values()):
        result = result + value
    return result

first_group = ["draft"]
print(combine_values(first_group, ["review"], final=["release"]))
print(first_group)
print(combine_values("A", middle="B", last="C"))
print(combine_values(2, 3, bonus=4))
print(combine_values(first_group) is first_group)
try:
    combine_values()
except TypeError:
    print("at least one positional value is required")
try:
    combine_values("count: ", 4)
except TypeError:
    print("each pair must support addition")
