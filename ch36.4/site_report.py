# site_report.py
import csv
from datetime import datetime, timezone
from functools import partial
from pathlib import Path
from tempfile import TemporaryDirectory

from aligned_records import FileSpec, aligned_records, ranked_groups, tied_leaders

def utc_stamp(text):
    # A literal Z declares UTC; strptime alone leaves tzinfo unset.
    return datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc)

def current_in(row, *, since, region):
    return row.updated >= since and row.region == region

def fixture_specs(folder):
    # Configuration pairs each file with its own schema, not parallel lists.
    entries = [
        ("sites.csv", {"site_id": str, "region": str, "label": str},
         [["S1", "North", "Hall, upper"], ["S2", "North", "Workshop"],
          ["S3", "North", "Store"], ["S4", "South", "Office"],
          ["S5", "South", "Annex"], ["S6", "South", "Old shed"]]),
        ("devices.csv", {"maker": str, "year": int, "site_id": str},
         [["Pine", "2024", "S1"], ["Cedar", "2023", "S2"],
          ["Pine", "2022", "S3"], ["Cedar", "2025", "S4"],
          ["Cedar", "2024", "S5"], ["Pine", "2020", "S6"]]),
        ("service.csv", {"site_id": str, "team": str, "hours": int},
         [["S1", "A", "0"], ["S2", "B", "3"], ["S3", "A", "4"],
          ["S4", "C", "2"], ["S5", "C", "5"], ["S6", "B", "6"]]),
        ("changes.csv", {"site_id": str, "updated": utc_stamp,
                         "created": utc_stamp},
         [[site, updated, "2025-01-01T00:00:00Z"] for site, updated in (
             ("S1", "2026-06-01T00:00:00Z"),
             ("S2", "2026-06-02T10:00:00Z"),
             ("S3", "2026-05-31T23:59:59Z"),
             ("S4", "2026-06-03T12:00:00Z"),
             ("S5", "2026-06-04T12:00:00Z"),
             ("S6", "2026-01-01T00:00:00Z"))]),
    ]
    specs = []
    for name, converters, data in entries:
        path = Path(folder) / name
        with path.open("w", encoding="utf-8", newline="") as target:
            csv.writer(target).writerows([list(converters), *data])
        specs.append(FileSpec(path, converters))
    return specs

def main():
    cutoff = datetime(2026, 6, 1, tzinfo=timezone.utc)
    with TemporaryDirectory() as folder:
        specs = fixture_specs(folder)
        with aligned_records(specs) as rows:
            first = next(rows)
            print("first:", first.site_id, first.label, first.year,
                  first.updated.isoformat())
            print("key copies:", first._fields.count("site_id"))
        for region in ("North", "South"):
            with aligned_records(specs) as rows:
                ranking = ranked_groups(
                    rows, accept=partial(current_in, since=cutoff, region=region),
                    key=lambda row: row.maker)
            print(region, ranking, "leaders:", tied_leaders(ranking))
        with aligned_records(specs, fields=("maker", "site_id")) as rows:
            print("projection:", next(rows))

if __name__ == "__main__":
    main()
