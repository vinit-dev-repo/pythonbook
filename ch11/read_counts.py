# read_counts.py
from pathlib import Path
import sys

path = Path(sys.argv[1])
with path.open(encoding="utf-8") as file:
    for line in file:
        print(line.removesuffix("\n"))
