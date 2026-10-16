from markupsafe import escape

@app.route("/search")
def search():
    term = request.args.get("q", "")
    rows = connection.execute(
        "SELECT title FROM books WHERE title LIKE ?", (f"%{term}%",)
    ).fetchall()
    titles = "".join(f"<p>{escape(r[0])}</p>" for r in rows)
    return f"<h1>Results for {escape(term)}</h1>" + titles
