from dateutil import parser
from dateutil.relativedelta import relativedelta

# 1
date = parser.parse("2026-09-15")
print(date + relativedelta(months=1))
