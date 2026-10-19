import sys

# The short way
with open("diary.txt") as f:
    text = f.read()
    print(len(text))

# The long way -- what "with" does underneath
manager = open("diary.txt")     # a file object IS its own context manager
value = manager.__enter__()     # only if THIS succeeds is __exit__ ever owed
hit_error = False
try:
    text = value.read()
    print(len(text))
except BaseException:
    hit_error = True
    # __exit__ is TOLD what went wrong. If it returns something truthy, it is
    # saying "I have handled this" and the error stops here; otherwise it flies on.
    if not manager.__exit__(*sys.exc_info()):
        raise
finally:
    if not hit_error:
        manager.__exit__(None, None, None)
