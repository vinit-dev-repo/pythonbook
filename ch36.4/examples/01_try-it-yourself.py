from contextlib import ExitStack, contextmanager

# 1
values = [0, "", None, "East"]
print([bool(value) for value in values])
print([value is not None for value in values])
print(all(value is not None for value in values[:2]))

# 2
@contextmanager
def numbers(count):
    def counting():
        for i in range(count):
            yield i

    stream = counting()
    try:
        yield stream
    finally:
        stream.close()

with numbers(5) as stream:
    print(next(stream))
print(list(stream))

# 3
sites_a = ["S1", "S2", "S3"]
sites_b = ["S1", "S2"]
try:
    list(zip(sites_a, sites_b, strict=True))
except ValueError as error:
    print("lengths differ:", error)

for left, right in zip(["S1", "S2"], ["S1", "S9"], strict=True):
    if left != right:
        print("rows refer to different keys:", left, right)

# 4
with ExitStack() as stack:
    for name in ("files", "streams", "report"):
        stack.callback(print, "closing", name)
    print("working")
