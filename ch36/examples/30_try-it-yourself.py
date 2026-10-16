# 1
class AnnouncingFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("file closed, no matter what:", self.file.closed)

with AnnouncingFile("diary.txt", "w") as f:
    f.write("Dear diary...\n")

try:
    with AnnouncingFile("diary.txt", "w") as f:
        f.write("before the failure\n")
        1 / 0
except ZeroDivisionError:
    assert f.closed
    print("original division error reached the caller")

# 2
class Announcer:
    def __enter__(self):
        print("starting!")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("finished!")

with Announcer():
    print("doing thing one")
    print("doing thing two")

# 3
class Announcer2:
    def __enter__(self):
        print("starting!")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, ZeroDivisionError):
            print("caught a division error")
            return True
        print("finished!")
        return False

with Announcer2():
    1 / 0

original = ValueError("keep this failure")
try:
    with Announcer2():
        raise original
except ValueError as error:
    assert error is original

# 4
from contextlib import contextmanager

@contextmanager
def loud_mode():
    print("ENTERING LOUD MODE")
    try:
        yield
    finally:
        print("leaving loud mode")

with loud_mode():
    print("HELLO!")

# 5
from contextlib import ExitStack
from pathlib import Path

for name in ["1.txt", "2.txt", "3.txt"]:
    Path(name).write_text(name)

with ExitStack() as stack:
    files = [stack.enter_context(open(name)) for name in ["1.txt", "2.txt", "3.txt"]]
    for f in files:
        print(f.read())
