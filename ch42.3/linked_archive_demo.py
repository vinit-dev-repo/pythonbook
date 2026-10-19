# linked_archive_demo.py
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from linked_archive import Archive, Display, load_archive

rows = [
    {"kind": "place", "id": "north", "name": "North room"},
    {"kind": "piece", "id": "rain", "name": "Rain study"},
    {"kind": "piece", "id": "light", "name": "Light study"},
    {"kind": "display", "id": "weather", "name": "Weather studies",
     "place": "north", "pieces": ["rain", "light"]},
]
with TemporaryDirectory() as folder:
    path = Path(folder) / "archive"
    load_archive(path, json.dumps(rows))
    with Archive(path) as archive:
        display = archive.fetch("display:weather")
        print(isinstance(display, Display), display.name)
        print(display["place"], display["pieces"])
        print(display.place.name)
        print(display.place.name, archive.fetches)
        pieces = display.pieces
        print([piece.name for piece in pieces], archive.fetches)
        print(display.pieces is pieces, archive.fetches)
        del display.pieces
        print(display.pieces is pieces, archive.fetches)
    print(display.name, len(display.pieces))
    try:
        display.place
    except RuntimeError:
        print("live lookup needs an open archive")
