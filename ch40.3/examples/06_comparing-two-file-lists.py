from pathlib import Path

expected_files = {"main.py", "utils.py", "config.py"}
actual_files = {p.name for p in Path(".").glob("*.py")}   # comprehension recap

missing = expected_files - actual_files
extra = actual_files - expected_files

print("Missing files:", sorted(missing))
print("Unexpected extra files:", sorted(extra))
