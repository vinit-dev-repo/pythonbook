import itertools

print(list(itertools.repeat("hi", 3)))

zeros = itertools.repeat(0)
print(list(itertools.islice(zeros, 5)))
