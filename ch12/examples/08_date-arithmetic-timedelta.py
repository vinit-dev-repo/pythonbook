from datetime import date, timedelta

today = date(2026, 8, 30)          # a fixed date, so this example prints the same for everyone
next_week = today + timedelta(days=7)
print(next_week)

deadline = date(2026, 12, 25)
days_left = (deadline - today).days
print(days_left)
