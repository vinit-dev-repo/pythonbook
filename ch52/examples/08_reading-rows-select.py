import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.execute("SELECT * FROM products ORDER BY id")
for row in cursor:
    print(row)

connection.close()
