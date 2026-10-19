from contextlib import ExitStack, contextmanager, suppress
from pathlib import Path

# 1
names = ["1.txt", "2.txt", "3.txt"]
for name in names:
    Path(name).write_text(name)

with ExitStack() as stack:
    files = [stack.enter_context(open(name)) for name in names]
    for f in files:
        print(f.read())
print([f.closed for f in files])

# 2
class Step:
    def __init__(self, name, fail=False):
        self.name = name
        self.fail = fail

    def __enter__(self):
        print("enter", self.name)
        if self.fail:
            raise RuntimeError(self.name + " failed to start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit", self.name)

with Step("A"), Step("B"):
    print("inside")

# 3
try:
    with Step("A"), Step("B", fail=True):
        print("inside")
except RuntimeError as error:
    print("caught:", error)

# 4
@contextmanager
def quiet_keys(log):
    log.append("enter")
    try:
        yield
    except KeyError:
        log.append("handled KeyError")
    finally:
        log.append("exit")

log = []
with quiet_keys(log):
    {}["missing"]
print(log)

log = []
try:
    with quiet_keys(log):
        int("x")
except ValueError:
    print("ValueError went through:", log)

# 5
settings = {}
with suppress(KeyError):
    print(settings["theme"])
print("still running")
