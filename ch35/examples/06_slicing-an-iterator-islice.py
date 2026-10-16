import itertools

print(list(itertools.islice(iter([10, 20, 30, 40, 50]), 2)))   # stop=2 (no start given)
print(list(itertools.islice(iter("abcdefgh"), 2, 6)))          # start=2, stop=6
print(list(itertools.islice(range(20), 0, 20, 2)))             # start, stop, step=2
