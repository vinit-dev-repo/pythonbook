# 1
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hi = make_greeter("Hi")
print(say_hi("Sam"))                 # Hi, Sam!

# 2
counter = 0
def broken():
    print(counter)
    counter = counter + 1
# broken()   # would raise UnboundLocalError

def fixed():
    global counter
    print(counter)
    counter = counter + 1

fixed()
fixed()
print(counter)                        # 0, then 1, then final counter is 2

# 3
functions = []
for i in range(4):
    functions.append(lambda: i)
print([f() for f in functions])       # [3, 3, 3, 3] - the trap

functions = []
for i in range(4):
    functions.append(lambda i=i: i)
print([f() for f in functions])       # [0, 1, 2, 3] - fixed

# 4
from functools import reduce
words = ["cat", "elephant", "dog"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest)                         # elephant

# 5
from functools import partial

def print_upper(text, *, end):
    print(text.upper(), end=end)

shout = partial(print_upper, end="!!!\n")
shout("hello")                         # HELLO!!!
