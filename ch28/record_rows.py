# record_rows.py
from collections import namedtuple

def rows_to_records(rows):
    rows = list(rows)
    if not rows:
        return []

    names = set()
    for row in rows:
        for name in row:
            names.add(name)
    fields = sorted(names)
    Row = namedtuple("Row", fields, defaults=(None,) * len(fields))
    return [Row(**row) for row in rows]
