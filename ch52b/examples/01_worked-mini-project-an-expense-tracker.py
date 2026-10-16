import sqlite3
from contextlib import closing
from datetime import date

DB_FILE = "expenses.db"


def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def setup():
    with closing(get_connection()) as connection, connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                description TEXT,
                category TEXT,
                amount REAL,
                spent_on TEXT
            )
        """)


def add_expense(description, category, amount, spent_on):
    with closing(get_connection()) as connection, connection:
        connection.execute(
            """INSERT INTO expenses (description, category, amount, spent_on)
               VALUES (?, ?, ?, ?)""",
            (description, category, amount, spent_on)
        )


def list_by_category(category):
    with closing(get_connection()) as connection, connection:
        cursor = connection.execute(
            "SELECT * FROM expenses WHERE category = ? ORDER BY spent_on",
            (category,)
        )
        return cursor.fetchall()


def monthly_total(year_month):
    # year_month looks like "2026-08"
    with closing(get_connection()) as connection, connection:
        cursor = connection.execute(
            "SELECT SUM(amount) AS total FROM expenses WHERE spent_on LIKE ?",
            (f"{year_month}%",)
        )
        return cursor.fetchone()["total"] or 0.0


setup()
add_expense("Bus ticket", "Transport", 3.50, str(date(2026, 8, 1)))
add_expense("Lunch", "Food", 8.20, str(date(2026, 8, 2)))
add_expense("Train ticket", "Transport", 12.00, str(date(2026, 8, 15)))

print("Transport expenses:")
for row in list_by_category("Transport"):
    print(f"  {row['spent_on']}: {row['description']} — £{row['amount']}")

print(f"August total: £{monthly_total('2026-08'):.2f}")
