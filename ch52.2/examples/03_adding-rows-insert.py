import sqlite3

connection = sqlite3.connect("shop.db")

new_products = [
    ("Toaster", 18.50),
    ("Blender", 32.00),
    ("Mug", 4.25),
]
connection.executemany(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    new_products
)
connection.commit()
connection.close()
