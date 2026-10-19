import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "checks.db"
    with (
        closing(sqlite3.connect(path, autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL)) as writer,
        closing(sqlite3.connect(path, autocommit=True)) as observer,
    ):
        writer.execute("CREATE TABLE checks (label TEXT NOT NULL)")
        print("table visible:", observer.execute(
            "SELECT name FROM sqlite_master WHERE name = 'checks'"
        ).fetchone()[0])
        writer.execute("INSERT INTO checks VALUES (?)", ("door checked",))
        try:
            writer.execute("SELEC label FROM checks")  # deliberately misspelled SQL
        except sqlite3.OperationalError:
            print("SQL syntax failed; Python reached execute")
        print("writer sees:", writer.execute("SELECT count(*) FROM checks").fetchone()[0])
        print("observer sees:", observer.execute("SELECT count(*) FROM checks").fetchone()[0])
        writer.rollback()
        print("after rollback:", writer.execute("SELECT count(*) FROM checks").fetchone()[0])
        writer.execute("INSERT INTO checks VALUES (?)", ("window checked",))
        writer.commit()
        cursor = writer.cursor()
        writer.close()
        try:
            cursor.execute("SELECT label FROM checks")
        except sqlite3.ProgrammingError:
            print("closed connection rejected")
        print("committed row:", observer.execute("SELECT label FROM checks").fetchone()[0])
