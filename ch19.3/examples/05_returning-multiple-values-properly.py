from collections import namedtuple

Stats = namedtuple("Stats", "minimum maximum average")

def analyse(numbers):
    return Stats(min(numbers), max(numbers), sum(numbers) / len(numbers))

result = analyse([4, 8, 15, 16, 23, 42])
print(result)
print(result.average)
