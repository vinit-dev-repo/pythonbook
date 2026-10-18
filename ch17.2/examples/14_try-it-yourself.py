# 1
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hi = make_greeter("Hi")
print(say_hi("Sam"))                  # Hi, Sam!

# 2
functions = []
for i in range(4):
    functions.append(lambda: i)
print([f() for f in functions])       # [3, 3, 3, 3] - the trap

functions = []
for i in range(4):
    functions.append(lambda i=i: i)
print([f() for f in functions])       # [0, 1, 2, 3] - fixed

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

print([f() for f in make_four_late()])        # [3, 3, 3, 3]
print([f() for f in make_four_defaults()])    # [0, 1, 2, 3]

# 3
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

first = make_counter()
second = make_counter()
print(first(), first(), second(), first())    # 1 2 1 3

# 4
def make_accumulator():
    total = 0
    def add(amount):
        nonlocal total
        total += amount
        return total
    return add

running_total = make_accumulator()
print(running_total(10), running_total(5), running_total(20))   # 10 15 35
print(running_total.__closure__[0].cell_contents)               # 35
