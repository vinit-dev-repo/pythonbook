# package_api/check_zip.py
from pathlib import Path
from zipfile import ZipFile
import sys

root = Path(__file__).resolve().parent
archive = root / "myapp.zip"
with ZipFile(archive, "w") as bundle:
    for source in sorted((root / "myapp").rglob("*.py")):
        bundle.write(source, source.relative_to(root).as_posix())
sys.path.insert(0, str(archive))
import myapp
print(myapp.shout_number(42))
print("myapp.zip" in myapp.__file__)
print("myapp.zip" in myapp.utils.numbers.__file__)
