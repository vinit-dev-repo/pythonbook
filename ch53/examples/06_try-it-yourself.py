from flask import Flask, render_template, jsonify

app = Flask(__name__)
my_list = ["a", "b", "c"]
todos = [
    {"id": 1, "task": "Learn Flask", "done": True},
    {"id": 2, "task": "Build an API", "done": False},
]


# 1
@app.route("/contact")
def contact():
    return "Contact us at hello@example.com"


# 2
@app.route("/double/<int:number>")
def double(number):
    return str(number * 2)


# 3
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


# 4
@app.route("/count")
def count():
    return jsonify({"total": len(my_list)})


# 5
@app.route("/todos/done")
def done_todos():
    return jsonify([t for t in todos if t["done"]])
