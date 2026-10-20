from pathlib import Path

path = Path("notes.txt")
path.write_text("hello")

# Pythonic — closes automatically, even on error
with path.open() as f:
    print(f.read())
