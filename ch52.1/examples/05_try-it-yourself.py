import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

# 1
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE notes (text TEXT)")
connection.execute("INSERT INTO notes VALUES ('first')")
connection.rollback()
print("after rollback:", connection.execute("SELECT count(*) FROM notes").fetchone()[0])
connection.execute("INSERT INTO notes VALUES ('second')")
connection.commit()
print("after commit:", connection.execute("SELECT count(*) FROM notes").fetchone()[0])
connection.close()

# 2
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE notes (text TEXT NOT NULL)")
try:
    with connection:
        connection.execute("INSERT INTO notes VALUES ('valid')")
        connection.execute("INSERT INTO notes VALUES (NULL)")
except sqlite3.IntegrityError:
    print("second insert failed")
print("rows:", connection.execute("SELECT count(*) FROM notes").fetchone()[0])
connection.close()

# 3
with TemporaryDirectory() as directory:
    path = Path(directory) / "notes.db"
    with closing(sqlite3.connect(path)) as connection:
        connection.execute("CREATE TABLE notes (text TEXT)")
        connection.execute("INSERT INTO notes VALUES ('lost')")
    with closing(sqlite3.connect(path)) as connection:
        print("after closing without commit:", connection.execute("SELECT count(*) FROM notes").fetchone()[0])
        connection.execute("INSERT INTO notes VALUES ('kept')")
        connection.commit()
    with closing(sqlite3.connect(path)) as connection:
        print("after commit and reopen:", connection.execute("SELECT count(*) FROM notes").fetchone()[0])
