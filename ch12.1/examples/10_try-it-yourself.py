# 1
from datetime import date
print(date.today().strftime("%d %B %Y"))

# 2
from datetime import date, timedelta
today = date.today()
new_year = date(today.year + 1, 1, 1)
print((new_year - today).days)

# 3
import time
start = time.perf_counter()
sum(range(1_000_000))
print(f"{time.perf_counter() - start:.3f} seconds")

# 4
from datetime import datetime
parsed = datetime.strptime("07:05 PM / 2026-04-09", "%I:%M %p / %Y-%m-%d")
print(parsed.hour)     # 19

# 5
from datetime import datetime, timezone
naive = datetime(2026, 8, 30)
aware = datetime(2026, 8, 30, tzinfo=timezone.utc)
print(naive == aware)  # False
try:
    naive < aware
except TypeError as error:
    print("TypeError:", error)
