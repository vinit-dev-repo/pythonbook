# 2
try:
    broken()
except UnboundLocalError:
    print("UnboundLocalError: counter is local before assignment")

# 3
def make_four_late():
    functions = []
    for i in range(4):
        functions.append(lambda: i)
    return functions

def make_four_defaults():
    functions = []
    for i in range(4):
        functions.append(lambda i=i: i)
    return functions

print([f() for f in make_four_late()])
print([f() for f in make_four_defaults()])

# 6
first = make_counter()
second = make_counter()
print(first(), first(), second(), first())
print(reduce(lambda acc, n: acc + n, [], 0))
