a = "hello"
b = "hello"
print(a is b)            # often True — short, identifier-like strings are commonly interned

x = "hello there!"
y = "".join(["hello ", "there!"])   # built at RUNTIME - not the same literal the compiler saw
print(x is y)             # False - a freshly built string is a new object, even if it reads identically
