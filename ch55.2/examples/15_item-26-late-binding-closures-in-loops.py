makers = [lambda i=i: i for i in range(3)]
print([m() for m in makers])
