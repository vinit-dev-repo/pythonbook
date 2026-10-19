import shelve
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = str(Path(folder) / "settings")
    with shelve.open(path) as db:          # writes to disk
        db["theme"] = "dark"
        db["recent"] = ["a.txt", "b.txt"]

    with shelve.open(path) as db:          # a completely separate open
        print(db["theme"])
        print(db["recent"])
        print(sorted(db.keys()))
        print("missing" in db)
