# managed_csv_records.py
import csv
from collections import defaultdict, namedtuple
from contextlib import contextmanager
from datetime import datetime
from functools import partial
from pathlib import Path
from tempfile import TemporaryDirectory

def prepare_reader(source, delimiter=None):
    if delimiter is None:
        dialect = csv.Sniffer().sniff(source.read(4096), delimiters=",;\t|")
        source.seek(0)
        reader = csv.reader(source, dialect, strict=True)
    else:
        reader = csv.reader(source, delimiter=delimiter, strict=True)
    header = next(reader, None)
    if not header:
        raise ValueError("a nonempty header is required")
    names = ["_".join(label.split()).lower() for label in header]
    row_type = namedtuple("Row", names)  # rejects duplicate/invalid names
    return reader, row_type

def pack_row(reader, row_type):
    cells = next(reader)
    if len(cells) != len(row_type._fields):
        raise ValueError("record width does not match header")
    return row_type(*cells)

class CSVRows:
    def __init__(self, path, delimiter=None):
        self.path = path
        self.delimiter = delimiter
        self._state = "new"
        self._source = None
        self._ended = False

    def __enter__(self):
        if self._state != "new":
            raise RuntimeError("create a fresh manager for each with block")
        self._state = "entering"
        try:
            self._source = open(self.path, encoding="utf-8", newline="")
            self._reader, self._row_type = prepare_reader(
                self._source, self.delimiter)
        except BaseException:
            if self._source is not None:
                self._source.close()
            self._state = "closed"
            raise
        self._state = "active"
        return self

    def __exit__(self, kind, error, traceback):
        self._state = "closed"
        self._source.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._state == "new":
            raise RuntimeError("enter the context before reading")
        if self._state != "active" or self._ended:
            raise StopIteration
        try:
            return pack_row(self._reader, self._row_type)
        except StopIteration:
            self._ended = True
            raise

@contextmanager
def managed_rows(path, delimiter=None):
    with open(path, encoding="utf-8", newline="") as source:
        reader, row_type = prepare_reader(source, delimiter)

        def unpacked_rows():
            while True:
                try:
                    row = pack_row(reader, row_type)
                except StopIteration:
                    return
                yield row

        rows = unpacked_rows()
        try:
            yield rows
        finally:
            rows.close()

def integer_or_none(text):
    try:
        return int(text)
    except ValueError:
        return None

def date_or_none(text, format="%Y-%m-%d"):
    try:
        return datetime.strptime(text.strip(), format).date()
    except ValueError:
        return None

def clean_text(text, default=None):
    return text.strip() or default

def converted_rows(rows, converters, reject):
    for number, row in enumerate(rows, start=2):
        if set(row._fields) != set(converters):
            raise ValueError("header does not match the conversion schema")
        values = [converters[name](text)
                  for name, text in zip(row._fields, row, strict=True)]
        if all(value is not None for value in values):
            yield type(row)(*values)
        else:
            reject(number, row)

def count_zones(records):
    counts = defaultdict(int)
    for record in records:
        counts[record.zone] += 1
    return dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])))

SCHEMA = {
    "inspection_id": integer_or_none,
    "checked_on": date_or_none,
    "zone": clean_text,
    "note": partial(clean_text, default=""),
}

def conversion_traps():
    def broken(text, caught):
        try:
            return int(undefined_value)  # deliberate wrong name
        except caught:
            return None

    print("broad catch:", broken("7", Exception))
    try:
        broken("7", ValueError)
    except NameError:
        print("narrow catch: NameError; repaired:", integer_or_none("7"))
    values = (value for value in (0, ""))
    assert all(value is not None for value in values)
    Pair = namedtuple("Pair", "count note")
    try:
        Pair(*values)
    except TypeError:
        print("consumed conversion: TypeError")
    values = [0, ""]
    assert all(value is not None for value in values)
    print("saved conversion:", Pair(*values), "truthiness:", all(values))

def main():
    conversion_traps()
    header = ["Inspection ID", "Checked On", "Zone", "Note"]
    data = [
        ["10", "2026-05-01", "East", ""],
        ["11", "2026-05-02", "East", "lobby, north"],
        ["0", "2026-05-03", "West", ""],
        ["12", "2026-02-30", "East", "bad date"],
        ["13", "2026-05-04", " ", "missing zone"],
        ["14", "2026-05-05", "West", "follow-up"],
    ]
    with TemporaryDirectory() as folder:
        paths = []
        for name, delimiter in (("comma.csv", ","), ("semi.csv", ";")):
            path = Path(folder) / name
            with path.open("w", encoding="utf-8", newline="") as target:
                csv.writer(target, delimiter=delimiter,
                           quoting=csv.QUOTE_ALL).writerows([header, *data])
            paths.append(path)
        for factory in (CSVRows, managed_rows):
            for path in paths:
                rejected = []  # small demo only; a real callback can just count
                with factory(path) as raw:
                    counts = count_zones(converted_rows(
                        raw, SCHEMA, lambda number, row: rejected.append(number)))
                assert list(raw) == []
                print(factory.__name__, path.name, counts, rejected)
        with managed_rows(paths[0]) as raw:
            first = next(converted_rows(raw, SCHEMA, lambda *args: None))
            print("types:", type(first.inspection_id).__name__,
                  type(first.checked_on).__name__, type(first.note).__name__)

if __name__ == "__main__":
    main()
