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
