from datetime import datetime
from zoneinfo import ZoneInfo

ny_time = datetime(2024, 7, 4, 12, 0, tzinfo=ZoneInfo("America/New_York"))
print(ny_time)
print(ny_time.tzname())
