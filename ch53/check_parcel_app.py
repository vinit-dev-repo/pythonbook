# check_parcel_app.py
from parcel_app import app


def main():
    client = app.test_client()
    form = client.get("/pack")
    assert form.status_code == 200 and b'name="items"' in form.data
    sent = client.post("/pack", data={"items": "17", "capacity": "6"})
    assert sent.status_code == 303 and sent.headers["Location"] == "/plan/17/6"
    page = client.get(sent.headers["Location"])
    assert page.status_code == 200
    assert b"<dt>boxes</dt><dd>3</dd>" in page.data
    assert b"The last box holds 5 items." in page.data
    assert b"this comment is not sent" not in page.data
    assert b"No boxes needed." in client.get("/plan/0/6").data
    assert b"Every box is full." in client.get("/plan/18/6").data
    for data in ({}, {"items": "-1", "capacity": "6"},
                 {"items": "1.5", "capacity": "6"},
                 {"items": "17", "capacity": "0"}):
        assert client.post("/pack", data=data).status_code == 400
    assert client.get("/plan/17/0").status_code == 400
    assert client.get("/plan/word/6").status_code == 404
    assert client.put("/pack").status_code == 405
    print("form, redirect, result branches and invalid inputs: checked")


if __name__ == "__main__":
    main()
