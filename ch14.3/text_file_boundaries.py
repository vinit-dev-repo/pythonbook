# text_file_boundaries.py
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "lines.txt"
    raw = b"one\r\ntwo\rthree\n"
    path.write_bytes(raw)
    with open(path, encoding="utf-8") as file:
        print(repr(file.read()))
    with open(path, encoding="utf-8", newline="") as file:
        print(file.read() == raw.decode("utf-8"))
    print(path.read_bytes() == raw)
    with open(path, "w", encoding="utf-8", newline="\r\n") as file:
        print("Characters written:", file.write("east\nwest\n"))
    print(path.read_bytes())
    for mode, value, options in (
        ("w", b"east", {"encoding": "utf-8"}),
        ("wb", "east", {}),
    ):
        with open(Path(folder) / "type_trial", mode, **options) as file:
            try:
                file.write(value)
            except TypeError:
                print(mode, "rejects", type(value).__name__)
