import contextlib
import io
from pathlib import Path

# 1
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
    print("the other error went through unchanged")

# 2
@contextlib.contextmanager
def loud_mode():
    print("ENTERING LOUD MODE")
    try:
        yield
    finally:
        print("leaving loud mode")

with loud_mode():
    print("HELLO!")

# 3
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    print("hello from inside the block")
print(buffer.getvalue().strip().upper())

# 4
Path("notes.txt").write_text("first line\nsecond line\n")

def lazy_version(path):
    with open(path) as f:
        return f

lines = lazy_version("notes.txt")
try:
    lines.readline()
except ValueError as error:
    print("lazy version fails:", error)

def first_line(path):
    with open(path) as f:
        return f.readline().strip()

print(first_line("notes.txt"))
