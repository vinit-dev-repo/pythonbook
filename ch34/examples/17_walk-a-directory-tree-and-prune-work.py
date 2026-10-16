import os
from pathlib import Path
from tempfile import TemporaryDirectory

def report_walk_error(error):
    raise error

with TemporaryDirectory() as folder:
    root = Path(folder)
    for relative in ["guide.txt", "live/note.txt", ".cache/hidden.txt"]:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("practice\n", encoding="utf-8")

    walk = os.walk(root, topdown=True, onerror=report_walk_error,
                   followlinks=False)
    print("one iterator:", iter(walk) is walk)
    for current, subdirectories, filenames in walk:
        subdirectories[:] = sorted(name for name in subdirectories
                                   if name != ".cache")
        for name in sorted(filenames):
            path = Path(current) / name
            print(path.relative_to(root).as_posix())
    print("remaining:", list(walk))
