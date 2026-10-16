from datetime import datetime
from zoneinfo import ZoneInfo

london_time = datetime(2026, 8, 23, 15, 0, tzinfo=ZoneInfo("Europe/London"))
tokyo_time = london_time.astimezone(ZoneInfo("Asia/Tokyo"))

print(london_time)
print(tokyo_time)
