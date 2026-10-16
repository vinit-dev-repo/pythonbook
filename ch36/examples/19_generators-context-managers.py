@contextmanager
def open_uppercase(path):
    f = open(path)
    try:
        yield f.read().upper()      # this becomes the "as" value
    finally:
        f.close()

with open_uppercase("diary.txt") as shout:
    print(shout)
