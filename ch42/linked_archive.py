# linked_archive.py
import json
import shelve
from functools import cached_property

def load_archive(path, text):
    rows = json.loads(text)
    if type(rows) is not list:
        raise ValueError("expected a list of rows")
    prepared = {}
    shapes = {"place": {"kind", "id", "name"},
              "piece": {"kind", "id", "name"},
              "display": {"kind", "id", "name", "place", "pieces"}}
    for row in rows:
        if type(row) is not dict or type(row.get("kind")) is not str:
            raise ValueError("expected a row with a text kind")
        kind = row["kind"]
        if kind not in shapes or set(row) != shapes[kind]:
            raise ValueError("unknown kind or wrong row fields")
        if any(type(row[k]) is not str or not row[k] for k in ("id", "name")):
            raise ValueError("id and name must be nonempty strings")
        if kind == "display":
            if type(row["place"]) is not str or not row["place"]:
                raise ValueError("place must be a nonempty identifier")
            if type(row["pieces"]) is not list or any(
                type(x) is not str or not x for x in row["pieces"]
            ):
                raise ValueError("pieces must be a list of identifiers")
        key = kind + ":" + row["id"]
        if key in prepared:
            raise ValueError("duplicate record key")
        prepared[key] = row
    with shelve.open(str(path), flag="c") as db:
        if len(db):
            raise ValueError("destination must be empty")
        db.update(prepared)

class Record:
    def __init__(self, row, archive):
        self._row = dict(row)
        self._archive = archive

    def __getitem__(self, key):
        return self._row[key]

    def __getattr__(self, name):
        try:
            return self._row[name]
        except KeyError:
            raise AttributeError(name) from None

class Display(Record):
    @property
    def place(self):
        return self._archive.fetch("place:" + self._row["place"])

    @cached_property
    def pieces(self):
        return tuple(self._archive.fetch("piece:" + key)
                     for key in self._row["pieces"])

class Archive:
    record_types = {"display": Display}

    def __init__(self, path):
        self.path = str(path)
        self._db = None
        self.fetches = 0

    def __enter__(self):
        if self._db is not None:
            raise RuntimeError("archive is already open")
        self._db = shelve.open(self.path, flag="r")
        return self

    def __exit__(self, exc_type, exc, traceback):
        db, self._db = self._db, None
        db.close()

    def fetch(self, key):
        if self._db is None:
            raise RuntimeError("archive is closed")
        row = self._db[key]
        self.fetches += 1
        cls = self.record_types.get(row["kind"], Record)
        return cls(row, self)
