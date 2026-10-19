# test_flask_responses.py
import notes_app
import routes_app
import template_app


def exact_body(response):
    assert response.status_code == 200
    assert response.mimetype == "text/html"
    assert response.get_data(as_text=True) == "Showing post number 42 (a whole number: int)"


def main():
    route = routes_app.app.test_client()
    exact_body(route.get("/post/42"))
    head = route.head("/post/42")
    assert head.status_code == 200
    assert head.mimetype == "text/html"
    assert head.data == b""
    options = route.options("/post/42")
    assert options.status_code == 200
    allowed = {method.strip() for method in options.headers["Allow"].split(",")}
    assert allowed == {"GET", "HEAD", "OPTIONS"}
    assert route.post("/post/42").status_code == 405
    assert route.get("/post/no").status_code == 404
    assert route.get("/post/-1").status_code == 404
    escaped = route.get("/user/%3Cb%3ENoor%20%26%20Co")
    assert escaped.status_code == 200
    assert escaped.mimetype == "text/html"
    assert escaped.get_data(as_text=True) == "Hello, &lt;b&gt;Noor &amp; Co!"

    page = template_app.app.test_client().get("/")
    assert page.status_code == 200
    assert page.mimetype == "text/html"
    body = page.get_data(as_text=True)
    for fragment in (
        "<!doctype html>", "<html>", "<body>", "</body>", "</html>",
        "<h1>Hello, Vinit!</h1>", "<li>Tea</li>", "<li>Milk</li>",
        "<li>Bread</li>", "You have 3 items.",
    ):
        assert fragment in body
    assert body.count("<li>") == 3

    saved_notes = list(notes_app.notes)
    saved_testing = notes_app.app.config["TESTING"]
    try:
        notes_app.notes.clear()
        notes_app.app.config["TESTING"] = True
        notes = notes_app.app.test_client()
        other = notes_app.app.test_client()
        empty = notes.get("/api/notes")
        assert empty.status_code == 200
        assert empty.mimetype == "application/json"
        assert empty.get_json() == []
        raw_note = "<b>Noor & Co</b>"
        added = notes.post("/add", data={"text": raw_note})
        assert added.status_code == 302
        assert added.headers["Location"] == "/"
        shared = other.get("/api/notes")
        assert shared.status_code == 200
        assert shared.mimetype == "application/json"
        assert shared.get_json() == [raw_note]
        rendered = notes.get("/")
        assert rendered.status_code == 200
        assert rendered.mimetype == "text/html"
        assert b"&lt;b&gt;Noor &amp; Co&lt;/b&gt;" in rendered.data
        assert raw_note.encode() not in rendered.data
        blank = notes.post("/add", data={"text": "   "})
        assert blank.status_code == 302
        assert notes_app.notes == [raw_note]
        assert notes.post("/add", data={}).status_code == 400
        assert notes_app.notes == [raw_note]
    finally:
        notes_app.notes[:] = saved_notes
        notes_app.app.config["TESTING"] = saved_testing
    print("offline clients observe routes, escaping, methods, and shared local notes")


if __name__ == "__main__":
    main()
