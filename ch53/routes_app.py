# routes_app.py
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/user/<name>")
def show_user(name):
    return f"Hello, {escape(name)}!"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Showing post number {post_id} (a whole number: {type(post_id).__name__})"


if __name__ == "__main__":
    app.run(debug=True)
