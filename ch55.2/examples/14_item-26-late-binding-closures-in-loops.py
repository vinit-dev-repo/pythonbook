makers = [lambda: i for i in range(3)]
print([m() for m in makers])   # not [0, 1, 2]!
