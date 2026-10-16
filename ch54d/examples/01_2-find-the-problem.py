@app.route("/search")
def search():
    term = request.args.get("q", "")
    rows = connection.execute(
        f"SELECT title FROM books WHERE title LIKE '%{term}%'"
    ).fetchall()
    return f"<h1>Results for {term}</h1>" + "".join(f"<p>{r[0]}</p>" for r in rows)
