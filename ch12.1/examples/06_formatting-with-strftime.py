from datetime import datetime

now = datetime(2026, 8, 23, 14, 7)
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A, %d %B %Y"))
print(now.strftime("%H:%M"))
