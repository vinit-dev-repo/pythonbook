import builtins

def inspect_batch(len, entries):
    print("reported size:", len)
    print("observed size:", builtins.len(entries))

inspect_batch(12, ["a", "b", "c"])
print(len(["a", "b"]))
