import sqlite3

connection = sqlite3.connect("shop.db")

connection.execute(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    ("Kettle", 24.99)
)
connection.commit()

cursor = connection.execute("SELECT * FROM products ORDER BY id")
print(cursor.fetchall())

connection.close()
