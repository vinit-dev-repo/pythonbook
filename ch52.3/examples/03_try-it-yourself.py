import sqlite3
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import Session, declarative_base

# 1
connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
print("foreign keys:", connection.execute("PRAGMA foreign_keys").fetchone()[0])
connection.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY)")
connection.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        author_id INTEGER NOT NULL REFERENCES authors(id)
    )
""")
try:
    connection.execute("INSERT INTO books (id, author_id) VALUES (1, 7)")
except sqlite3.IntegrityError:
    print("missing author rejected")
connection.execute("INSERT INTO authors (id) VALUES (7)")
connection.execute("INSERT INTO books (id, author_id) VALUES (1, 7)")
connection.commit()
print("books:", connection.execute("SELECT id, author_id FROM books").fetchall())
connection.close()

# 2
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as session:
    session.add_all([Author(name="Orwell"), Author(name="Austen")])
    session.commit()
    print(session.scalars(select(Author.name).order_by(Author.name)).all())
