import sqlite3

connection = sqlite3.connect("shop.db")

with connection:
    connection.execute("INSERT INTO greeting VALUES ('saved safely')")
# commit happened automatically here, because nothing went wrong

connection.close()
