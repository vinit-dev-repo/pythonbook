import sqlite3

connection = sqlite3.connect("shop.db")

connection.execute("DELETE FROM products WHERE name = 'Mug'")
connection.commit()

connection.close()
