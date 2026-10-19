import sqlite3

connection = sqlite3.connect("library.db")
connection.row_factory = sqlite3.Row

# 1
connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        read INTEGER
    )
""")

# 2
connection.executemany(
    "INSERT INTO books (title, author, read) VALUES (?, ?, ?)",
    [
        ("Dune", "Frank Herbert", 0),
        ("1984", "George Orwell", 1),
        ("Emma", "Jane Austen", 0),
    ]
)
connection.commit()

# 3
cursor = connection.execute("SELECT title FROM books WHERE read = 0")
for row in cursor:
    print(row["title"])

# 4
connection.execute("UPDATE books SET read = 1 WHERE title = 'Dune'")
connection.commit()

# 5
author = "George Orwell"
cursor = connection.execute("SELECT title FROM books WHERE author = ?", (author,))
for row in cursor:
    print(row["title"])

connection.close()
