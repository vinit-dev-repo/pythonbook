connection.execute(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    ("Kettle", 24.99)
)
