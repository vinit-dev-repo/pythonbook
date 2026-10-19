import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.execute("SELECT name FROM products WHERE id = 1")
print(cursor.fetchone())

connection.close()
