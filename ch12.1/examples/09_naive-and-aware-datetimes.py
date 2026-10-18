from datetime import datetime, timezone

naive = datetime(2026, 8, 30, 14, 7, 52)
aware = datetime(2026, 8, 30, 14, 7, 52, tzinfo=timezone.utc)

print(naive)
print(aware)
print(naive.tzinfo)
print(aware.tzinfo)
