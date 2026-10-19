import sqlite3

connection = sqlite3.connect("shop.db")   # the file appears on disk here
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS greeting (message TEXT)")
cursor.execute("INSERT INTO greeting VALUES ('hello, database')")
connection.commit()                        # required in the default legacy transaction mode

connection.close()
