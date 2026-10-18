# zip_demo/check.py
from pathlib import Path
from zipfile import ZipFile
import sys

root = Path(__file__).resolve().parent
archive = root / "modules.zip"
with ZipFile(archive, "w") as bundle:
    bundle.write(root / "archive_module.py", "archive_module.py")
sys.path.insert(0, str(archive))
import archive_module
print(archive_module.MESSAGE)
print("modules.zip" in archive_module.__file__)
