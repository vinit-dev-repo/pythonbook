# 1
from datetime import date
print(date.today().strftime("%d %B %Y"))

# 2
from datetime import date, timedelta
today = date.today()
new_year = date(today.year + 1, 1, 1)
print((new_year - today).days)

# 3
import csv
with open("people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Asha", 30])
    writer.writerow(["Ravi", 25])

with open("people.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])

# 4
import random
random.seed(7)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
# run it again -- same three numbers both times

# 5
from decimal import Decimal
total = Decimal("2.10") + Decimal("3.45")
print(total.quantize(Decimal("0.01")))   # 5.55
