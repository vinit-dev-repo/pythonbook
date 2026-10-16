from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
guestbook = []


@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        name = request.form["name"]
        guestbook.append(name)
        return redirect(url_for("sign"))
    return render_template("sign.html", names=guestbook)


if __name__ == "__main__":
    app.run(debug=True)
