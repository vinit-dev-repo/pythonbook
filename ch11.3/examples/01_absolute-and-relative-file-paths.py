from pathlib import Path

relative = Path("notes.txt")
absolute = relative.resolve()
print(relative.is_absolute())
print(absolute.is_absolute())
print(absolute.name)
