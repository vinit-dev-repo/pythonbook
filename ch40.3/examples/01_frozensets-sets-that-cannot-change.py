normal = {1, 2, 3}
frozen = frozenset([1, 2, 3])

frozen.add(4)     # error — frozensets have no .add
