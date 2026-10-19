import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

from flask import Flask, jsonify
from markupsafe import escape

# 1
app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello"


client = app.test_client()
print(client.get("/hello").status_code)
print(client.head("/hello").status_code)
print(client.post("/hello").status_code)
print(sorted(method.strip() for method in client.options("/hello").headers["Allow"].split(",")))

# 2
app = Flask(__name__)


@app.route("/user/<name>")
def show_user(name):
    return f"Hello, {escape(name)}!"


print(app.test_client().get("/user/%3Cb%3EAda").get_data(as_text=True))

# 3
with TemporaryDirectory() as directory:
    path = Path(directory) / "items.db"
    with closing(sqlite3.connect(path)) as connection, connection:
        connection.execute("CREATE TABLE items (name TEXT)")
        connection.executemany("INSERT INTO items VALUES (?)", [("pen",), ("book",)])

    app = Flask(__name__)

    @app.route("/items")
    def list_items():
        with closing(sqlite3.connect(path)) as connection:
            rows = connection.execute("SELECT name FROM items ORDER BY name").fetchall()
        return jsonify([name for (name,) in rows])

    response = app.test_client().get("/items")
    print(response.status_code, response.get_json())
