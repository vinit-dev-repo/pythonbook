small = {"read"}
large = {"read", "write"}
other = {"share"}
print(small <= small, small < small)
print(small < large, large > small)
print(small < other, small > other, small == other)
print(small.issubset(["read", "write"]))
frozen = frozenset({"read"})
print(type(frozen | large).__name__, type(large | frozen).__name__)
saved = frozen
frozen |= {"write"}
print(sorted(saved), sorted(frozen), saved is frozen)
