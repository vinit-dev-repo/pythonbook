print(hash((1, "a")) == hash((1, "a")))   # fine — a tuple of hashable things
print(hash((1, [2, 3])))                  # fails — the tuple contains a list
