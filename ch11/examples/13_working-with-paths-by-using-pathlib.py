from pathlib import Path

folder = Path("data")
file_path = folder / "notes.txt"     # the / joins path pieces together
print(file_path.as_posix())
print(file_path.exists())
