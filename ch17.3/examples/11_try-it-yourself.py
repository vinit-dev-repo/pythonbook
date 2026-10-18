import inspect
from functools import reduce

# 1
words = ["cat", "elephant", "dog"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest)                        # elephant

# 2
def schedule(job, /, retries=2, *, urgent=False):
    return job, retries, urgent

sig = inspect.signature(schedule)
for name, parameter in sig.parameters.items():
    print(name, parameter.kind.name)
bound = sig.bind("backup", urgent=True)
print(bound.arguments)
# job POSITIONAL_ONLY, retries POSITIONAL_OR_KEYWORD, urgent KEYWORD_ONLY
# {'job': 'backup', 'urgent': True}

# 3
prices = [3, 7, 2]
print(reduce(lambda acc, n: acc + n, prices, 0))    # 12
print(reduce(lambda acc, n: acc + n, [], 0))        # 0

# 4
def ping():
    ping.calls += 1

ping.calls = 0
for _ in range(3):
    ping()
print(ping.calls)                     # 3
