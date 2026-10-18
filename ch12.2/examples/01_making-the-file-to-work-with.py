import csv

# make the example file first, so everything below runs on its own
rows = [["name", "price", "quantity"],
        ["apples", "0.50", "10"],
        ["bread", "2.20", "3"]]
with open("shop.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)

print("shop.csv written")
