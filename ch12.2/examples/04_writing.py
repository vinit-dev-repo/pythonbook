import csv

rows = [
    {"name": "milk", "price": "1.50"},
    {"name": "eggs", "price": "2.00"},
]

with open("out.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price"])
    writer.writeheader()
    writer.writerows(rows)
