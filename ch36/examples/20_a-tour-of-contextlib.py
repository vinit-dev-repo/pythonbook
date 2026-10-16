from contextlib import suppress
from pathlib import Path

with suppress(FileNotFoundError):
    Path("does_not_exist.txt").unlink()   # silently does nothing if the file is missing

print("no crash, even though the file was never there")
