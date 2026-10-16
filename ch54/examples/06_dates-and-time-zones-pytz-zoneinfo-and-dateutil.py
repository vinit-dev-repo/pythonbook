from datetime import datetime
import pytz

naive = datetime(2026, 8, 23, 15, 0)         # no time zone info yet

london_tz = pytz.timezone("Europe/London")
london_time = london_tz.localize(naive)       # attach a time zone to a naive datetime

tokyo_tz = pytz.timezone("Asia/Tokyo")
tokyo_time = london_time.astimezone(tokyo_tz)  # convert to a different zone

print(london_time)
print(tokyo_time)
