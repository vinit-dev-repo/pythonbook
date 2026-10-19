import sqlite3

connection = sqlite3.connect("bank.db")
connection.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        name TEXT PRIMARY KEY,
        balance REAL
    )
""")
connection.execute("DELETE FROM accounts")
connection.executemany(
    "INSERT INTO accounts (name, balance) VALUES (?, ?)",
    [("Alice", 100.0), ("Bob", 50.0)]
)
connection.commit()


def transfer(sender, receiver, amount):
    try:
        connection.execute(
            "UPDATE accounts SET balance = balance - ? WHERE name = ?",
            (amount, sender)
        )
        connection.execute(
            "UPDATE accounts SET balance = balance + ? WHERE name = ?",
            (amount, receiver)
        )
        # a bug: this table was never created, so this always fails
        connection.execute(
            "INSERT INTO transfer_log (sender, receiver, amount) VALUES (?, ?, ?)",
            (sender, receiver, amount)
        )
        connection.commit()
        print("Transfer succeeded")
    except sqlite3.OperationalError as error:
        connection.rollback()
        print(f"Transfer failed and was undone: {error}")


transfer("Alice", "Bob", 30.0)

cursor = connection.execute("SELECT name, balance FROM accounts ORDER BY name")
for row in cursor:
    print(row)

connection.close()
