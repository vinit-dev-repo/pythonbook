from contextlib import ExitStack

names = ["a.txt", "b.txt", "c.txt"]
for n in names:
    Path(n).write_text(f"contents of {n}")

with ExitStack() as stack:
    files = [stack.enter_context(open(n)) for n in names]
    for f in files:
        print(f.read())
# every file in `files` is closed automatically here, even though there
# could have been 1 of them or 100 -- ExitStack tracks however many there are
