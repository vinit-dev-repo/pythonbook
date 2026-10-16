from datetime import date
from dateutil.relativedelta import relativedelta

start = date(2026, 1, 31)
print(start + relativedelta(months=1))   # a plain 31-day timedelta would overshoot into March
print(start + relativedelta(years=1, months=2))
