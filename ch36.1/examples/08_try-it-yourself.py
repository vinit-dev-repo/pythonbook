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
class Tracer:
    def __enter__(self):
        self.items = []
        return self.items

    def __exit__(self, exc_type, exc_value, traceback):
        print("the block added", len(self.items), "items")

with Tracer() as items:
    items.append("a")
    items.append("b")

# 4
class NeedsResource:
    def __enter__(self):
        raise RuntimeError("no resource")

    def __exit__(self, exc_type, exc_value, traceback):
        print("cleanup ran")

try:
    with NeedsResource():
        print("the body ran")
except RuntimeError as error:
    print("caught:", error)
