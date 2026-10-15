# exercise_flask_responses.py
import notes_app


def main():
    saved_notes = list(notes_app.notes)
    saved_testing = notes_app.app.config["TESTING"]
    try:
        notes_app.notes.clear()
        notes_app.app.config["TESTING"] = True
        client = notes_app.app.test_client()
        added = client.post("/add", data={"text": "<b>Noor & Co</b>"})
        assert added.status_code == 302
        assert added.headers["Location"] == "/"
        page = client.get("/")
        assert page.status_code == 200
        assert page.mimetype == "text/html"
        assert b"&lt;b&gt;Noor &amp; Co&lt;/b&gt;" in page.data
        assert b"<b>Noor & Co</b>" not in page.data
        stored = client.get("/api/notes")
        assert stored.status_code == 200
        assert stored.mimetype == "application/json"
        assert stored.get_json() == ["<b>Noor & Co</b>"]
        head = client.head("/api/notes")
        assert head.status_code == 200
        assert head.mimetype == "application/json"
        assert head.data == b""
        options = client.options("/add")
        assert options.status_code == 200
        allowed = {method.strip() for method in options.headers["Allow"].split(",")}
        assert allowed == {"POST", "OPTIONS"}
        assert client.head("/add").status_code == 405
        print("HTML escapes while JSON keeps the note text:", True)
        print("GET routes receive HEAD; POST-only routes reject it:", True)
    finally:
        notes_app.notes[:] = saved_notes
        notes_app.app.config["TESTING"] = saved_testing


if __name__ == "__main__":
    main()
