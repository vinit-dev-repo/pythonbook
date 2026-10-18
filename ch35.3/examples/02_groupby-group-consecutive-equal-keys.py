import itertools

sales = [
    ("East", 100),
    ("West", 200),
    ("East", 150),
    ("West", 90),
]

sales_sorted = sorted(sales, key=lambda row: row[0])

for region, group in itertools.groupby(sales_sorted, key=lambda row: row[0]):
    total = sum(amount for _, amount in group)
    print(region, total)
