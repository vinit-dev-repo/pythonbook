from contextlib import ExitStack
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    first_path = Path(folder) / "ready.txt"
    first_path.write_text("parcel ready", encoding="utf-8")
    paths = [first_path, Path(folder) / "missing.txt"]
    opened = []
    try:
        with ExitStack() as stack:
            for path in paths:
                opened.append(stack.enter_context(open(path, encoding="utf-8")))
            raise AssertionError("all paths should not open")
    except FileNotFoundError:
        print("opened:", len(opened))
        print("closed:", [file.closed for file in opened])
