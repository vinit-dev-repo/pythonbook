from functools import partial, reduce
from operator import itemgetter, mul

# 1
def print_upper(text, *, end):
    print(text.upper(), end=end)

shout = partial(print_upper, end="!!!\n")
shout("hello")                        # HELLO!!!

# 2
people = [("Amy", 30), ("Ben", 25), ("Cal", 35)]
print(sorted(people, key=itemgetter(1)))      # [('Ben', 25), ('Amy', 30), ('Cal', 35)]
print(reduce(mul, [1, 2, 3, 4]))              # 24

# 3
def charge(units, rate):
    return units * rate

standard = partial(charge, rate=3)
print(standard(4), standard(4, rate=5), standard(4))   # 12 20 12
print(standard.args, standard.keywords)                # () {'rate': 3}

# 4
def combine_values(first, /, *rest, **named):
    result = first
    for value in (*rest, *named.values()):
        result = result + value
    return result

print(combine_values(5, first=7))                      # 12
print(combine_values("X", last="Z", middle="Y"))       # XZY

# 5
delivered = []

def handler(message):
    delivered.append(message)

pending = [lambda: handler("opened"), lambda: handler("closed")]
print(delivered)                      # []
for action in pending:
    action()
print(delivered)                      # ['opened', 'closed']
