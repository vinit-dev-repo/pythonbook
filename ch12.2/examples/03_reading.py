import csv

with open("shop.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["price"])
