def broken_reader():
    yield next(iter(()))

def finished_reader():
    if False:
        yield 1
    return "complete"

try:
    next(broken_reader())
except RuntimeError as error:
    print(type(error).__name__, type(error.__cause__).__name__)

finished = finished_reader()
try:
    next(finished)
except StopIteration as end:
    print("returned:", end.value)
print("later:", next(finished, "exhausted"))
