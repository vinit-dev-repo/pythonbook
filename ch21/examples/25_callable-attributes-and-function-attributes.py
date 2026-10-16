class Formatter:
    shout = staticmethod(str.upper)   # keep class and instance access unbound

print(Formatter.shout("hello"))
print(Formatter().shout("hello"))
