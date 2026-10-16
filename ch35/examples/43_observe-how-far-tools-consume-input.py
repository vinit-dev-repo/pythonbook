import itertools

source = iter(range(8))
print("slice:", list(itertools.islice(source, 1, 6, 2)))
print("after slice:", next(source))

source = iter([2, 4, 7, 8])
print("prefix:", list(itertools.takewhile(lambda value: value % 2 == 0, source)))
print("after prefix:", list(source))

groups = itertools.groupby("aaabb")
first_key, first_group = next(groups)
second_key, second_group = next(groups)
print("old group:", first_key, list(first_group))
print("current group:", second_key, list(second_group))

print("empty totals:", list(itertools.accumulate([])))
print("initial total:", list(itertools.accumulate([], initial=10)))
