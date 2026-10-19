import sqlite3

connection = sqlite3.connect("shop.db")
connection.row_factory = sqlite3.Row

cursor = connection.execute("SELECT * FROM products WHERE id = 1")
row = cursor.fetchone()
print(row["name"], row["price"])

connection.close()
