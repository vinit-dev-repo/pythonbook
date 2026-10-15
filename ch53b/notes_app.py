# notes_app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
notes = []


@app.route("/")
def index():
    return render_template("notes.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    text = request.form["text"]
    if text.strip():
        notes.append(text)
    return redirect(url_for("index"))


@app.route("/api/notes")
def api_notes():
    return jsonify(notes)


if __name__ == "__main__":
    app.run(debug=True)
