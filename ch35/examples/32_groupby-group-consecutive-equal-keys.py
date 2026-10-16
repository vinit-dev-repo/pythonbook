import itertools

sales = [
    ("East", 100),
    ("West", 200),
    ("East", 150),   # East again, but NOT next to the first East
    ("West", 90),
]

# WRONG: not sorted by region first
for region, group in itertools.groupby(sales, key=lambda row: row[0]):
    total = sum(amount for _, amount in group)
    print(region, total)
