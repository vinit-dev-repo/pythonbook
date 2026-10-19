# template_app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", visitor_name="Vinit", items=["Tea", "Milk", "Bread"])


if __name__ == "__main__":
    app.run(debug=True)
