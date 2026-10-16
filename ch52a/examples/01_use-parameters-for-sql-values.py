import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE products (name TEXT, price REAL)")
