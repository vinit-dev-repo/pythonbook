import sqlite3

connection = sqlite3.connect("shop.db")
connection.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
""")
connection.execute("DELETE FROM products")   # start from an empty table every run
connection.commit()
connection.close()
