import tempfile
from pathlib import Path

# 3. A temporary directory that deletes itself when the block ends
with tempfile.TemporaryDirectory() as folder:
    scratch_file = Path(folder) / "scratch.txt"
    scratch_file.write_text("temporary!")
    print("exists while inside:", scratch_file.exists())

print("folder is gone now — nothing left to clean up by hand")
