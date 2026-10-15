# cli_demo/build_zip.py
from pathlib import Path
from zipfile import ZipFile

root = Path(__file__).resolve().parent
with ZipFile(root / "labels_app.zip", "w") as archive:
    for source in sorted((root / "app").glob("*.py")):
        archive.write(source, source.name)
print("labels_app.zip created")
