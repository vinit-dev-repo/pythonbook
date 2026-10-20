# exercise_zones.py
from datetime import datetime
from zoneinfo import ZoneInfo

UTC = ZoneInfo("UTC")
KOLKATA = ZoneInfo("Asia/Kolkata")

for month in (1, 7):
    new_york = datetime(2026, month, 15, 9, 30, tzinfo=ZoneInfo("America/New_York"))
    print(new_york.astimezone(UTC).isoformat())
    if month == 1:
        print(new_york.astimezone(KOLKATA).isoformat())
