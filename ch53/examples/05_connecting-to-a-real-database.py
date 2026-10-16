import sqlite3
from contextlib import closing
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/expenses")
def list_expenses():
    with closing(sqlite3.connect("expenses.db")) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.execute("SELECT * FROM expenses")
        rows = [dict(row) for row in cursor.fetchall()]
    return jsonify(rows)
