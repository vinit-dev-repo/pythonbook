import sqlite3

connection = sqlite3.connect("shop.db")

connection.execute("UPDATE products SET price = 21.99 WHERE name = 'Kettle'")
connection.commit()

cursor = connection.execute("SELECT * FROM products WHERE name = 'Kettle'")
print(cursor.fetchone())

connection.close()
