import itertools

groups = [["a", "b"], ["c"], ["d", "e", "f"]]
flat = itertools.chain.from_iterable(groups)
print(list(flat))
