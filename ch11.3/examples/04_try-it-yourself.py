# 1
from pathlib import Path
report = Path("output") / "report.csv"
print(report.exists())   # False, unless you actually have that file

# 2
from pathlib import Path
relative = Path("notes.txt")
print(relative.is_absolute())                  # False
print(relative.resolve().is_absolute())        # True
print(relative.resolve().name)                 # notes.txt

# 3
# From the folder that holds data, it finds data/notes.txt.
# From the folder above, it looks for a different, probably missing file
# and raises FileNotFoundError: a relative path depends on the working directory.
