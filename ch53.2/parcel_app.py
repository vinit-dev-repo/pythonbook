# parcel_app.py
"""Turn a validated packing request into a shareable result URL."""
from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)


def bounded_integer(text, lower):
    if not text or not text.isascii() or not text.isdecimal():
        abort(400, description="Enter whole decimal numbers.")
    if len(text) > 4:
        abort(400, description="Use at most four digits.")
    value = int(text)
    if value < lower:
        abort(400, description="The value is below its allowed minimum.")
    return value


@app.route("/pack", methods=["GET", "POST"])
def pack():
    if request.method == "POST":
        items = bounded_integer(request.form.get("items", ""), 0)
        capacity = bounded_integer(request.form.get("capacity", ""), 1)
        return redirect(url_for("plan", items=items, capacity=capacity), code=303)
    return render_template("parcel_form.html")


@app.get("/plan/<int:items>/<int:capacity>")
def plan(items, capacity):
    if items > 9999 or not 1 <= capacity <= 9999:
        abort(400, description="The result URL is outside the input bounds.")
    full, remainder = divmod(items, capacity)
    summary = {"items": items, "capacity": capacity,
               "boxes": full + (remainder != 0)}
    return render_template("parcel_result.html", summary=summary,
                           remainder=remainder)


if __name__ == "__main__":
    app.run()
