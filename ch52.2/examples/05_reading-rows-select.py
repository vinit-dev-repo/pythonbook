import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.execute(
    "SELECT name, price FROM products WHERE price < 20 ORDER BY price LIMIT 2"
)
for row in cursor:
    print(row)

connection.close()
