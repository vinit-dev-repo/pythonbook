from pathlib import Path

Path("notes.txt").write_text("Hello, this is a short file!")

with open("notes.txt") as f:
    for chunk in iter(lambda: f.read(8), ""):
        print(repr(chunk))
