# built at runtime, not typed as literals — this stops Python's compiler
# from silently folding the two into one shared constant
a = int("5000")
b = int("5000")
print(a == b)   # True — same value
print(a is b)   # False — NOT guaranteed to be the same object

x = 5
y = 5
print(x is y)   # True — small ints ARE cached, but don't rely on it
