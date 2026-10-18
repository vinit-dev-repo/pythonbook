import builtins

# 1
def bedroom():
    poster = "Python logo"
    print(poster)

bedroom()
try:
    print(poster)
except NameError as error:
    print(error)                      # name 'poster' is not defined

# 2
counter = 0

def broken():
    print(counter)
    counter = counter + 1

try:
    broken()
except UnboundLocalError:
    print("UnboundLocalError: counter is local before assignment")

def fixed():
    global counter
    print(counter)
    counter = counter + 1

fixed()
fixed()
print(counter)                        # 0, then 1, then the final value 2

# 3
def report(len, entries):
    print("reported size:", len)
    print("observed size:", builtins.len(entries))

report(5, ["a", "b"])                 # reported size: 5, observed size: 2

# 4
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        return x
    return inner(), x

print(outer(), x)                     # ('local', 'enclosing') global
