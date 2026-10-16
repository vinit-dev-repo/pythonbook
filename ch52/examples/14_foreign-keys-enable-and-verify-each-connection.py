import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temporary:
    database = Path(temporary) / "authors.db"
    with (
        closing(sqlite3.connect(database, autocommit=True)) as first,
        closing(sqlite3.connect(database, autocommit=True)) as second,
    ):
        first.execute("PRAGMA foreign_keys = OFF")
        second.execute("PRAGMA foreign_keys = OFF")
        first.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY)")
        first.execute("""
            CREATE TABLE books (
                id INTEGER PRIMARY KEY,
                author_id INTEGER NOT NULL REFERENCES authors(id)
            )
        """)

        first.execute("PRAGMA foreign_keys = ON")
        first_setting = first.execute("PRAGMA foreign_keys").fetchone()[0]
        second_setting = second.execute("PRAGMA foreign_keys").fetchone()[0]
        print(f"Settings: {first_setting} {second_setting}")

        second.execute("BEGIN")
        second.execute("PRAGMA foreign_keys = ON")
        print(f"Second inside transaction: {second.execute('PRAGMA foreign_keys').fetchone()[0]}")
        second.execute("ROLLBACK")
        second.execute("PRAGMA foreign_keys = ON")
        print(f"Second after rollback: {second.execute('PRAGMA foreign_keys').fetchone()[0]}")

        try:
            first.execute("INSERT INTO books (id, author_id) VALUES (?, ?)", (1, 99))
        except sqlite3.IntegrityError:
            print("Missing author rejected")

        first.execute("INSERT INTO authors (id) VALUES (?)", (99,))
        first.execute("INSERT INTO books (id, author_id) VALUES (?, ?)", (1, 99))
        print(
            "Shared books: "
            f"{second.execute('SELECT id, author_id FROM books ORDER BY id').fetchall()}"
        )

        try:
            second.execute("INSERT INTO books (id, author_id) VALUES (?, ?)", (2, 100))
        except sqlite3.IntegrityError:
            print("Second connection rejects missing author")
