# date_conversion_lab.py
import csv
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from dateutil import parser
import pytz


def closing_instant(day_text, zone):
    # This file format requires exactly DD/MM/YYYY, using ASCII digits.
    pieces = day_text.split("/")
    if (
        len(pieces) != 3
        or [len(piece) for piece in pieces] != [2, 2, 4]
        or not all(piece.isascii() and piece.isdecimal() for piece in pieces)
    ):
        raise ValueError("date must use DD/MM/YYYY")
    day = parser.parse(
        day_text, dayfirst=True, yearfirst=False,
        default=datetime(2000, 1, 1),
    )
    if day.strftime("%d/%m/%Y") != day_text:
        raise ValueError("date does not match the declared order")
    local = zone.localize(day.replace(hour=17), is_dst=None)
    return local.astimezone(pytz.UTC)


def convert_csv(source, target):
    if source.resolve() == target.resolve():
        raise ValueError("choose a separate output path")
    zone = pytz.timezone("Europe/Paris")
    converted = []
    with source.open(encoding="utf-8", newline="") as stream:
        rows = csv.reader(stream, strict=True)
        if next(rows, None) != ["day", "reading"]:
            raise ValueError("expected day,reading header")
        for row in rows:
            if len(row) != 2:
                raise ValueError("expected two fields per row")
            day_text, reading = row
            converted.append([closing_instant(day_text, zone).isoformat(), reading])
    # Validation finishes before the output is opened in overwrite mode.
    with target.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["closed_at_utc", "reading"])
        writer.writerows(converted)
    return len(converted)


def main():
    ambiguous = "04/05/2024"
    print(parser.parse(ambiguous, dayfirst=False).date())
    print(parser.parse(ambiguous, dayfirst=True).date())
    print(parser.parse("June", default=datetime(2000, 1, 15)).date())
    try:
        parser.parse("31 February 2024")
    except parser.ParserError:
        print("invalid calendar date")

    wall_time, ignored = parser.parse(
        "Logged: 14 June 2024 at 07:20 (station clock)",
        fuzzy_with_tokens=True, default=datetime(2000, 1, 1),
    )
    print(wall_time.isoformat())
    print("station clock" in "".join(ignored))
    zone_name = next(name for name in pytz.all_timezones if name == "Europe/Paris")
    zone = pytz.timezone(zone_name)
    print(zone.zone)
    utc = zone.localize(wall_time, is_dst=None).astimezone(pytz.UTC)
    print(utc.isoformat())
    print(utc.replace(tzinfo=None).isoformat())  # only for a legacy UTC-naive API
    for value in (datetime(2024, 3, 31, 2, 30), datetime(2024, 10, 27, 2, 30)):
        try:
            zone.localize(value, is_dst=None)
        except pytz.NonExistentTimeError:
            print("clock gap: ask for a valid time")
        except pytz.AmbiguousTimeError:
            print("clock overlap: ask which occurrence")

    with TemporaryDirectory() as directory:
        root = Path(directory)
        source, target = root / "readings.csv", root / "converted.csv"
        source.write_text(
            "day,reading\n15/01/2024,000.1250\n15/07/2024,2.5000\n",
            encoding="utf-8",
        )
        print("converted:", convert_csv(source, target))
        with target.open(encoding="utf-8", newline="") as stream:
            for row in csv.reader(stream):
                print(" | ".join(row))


if __name__ == "__main__":
    main()
