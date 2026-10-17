from pathlib import Path

# find paths whose names end in .txt in the current folder
for file in sorted(Path(".").glob("*.txt")):
    print(file)
