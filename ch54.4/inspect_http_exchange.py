# inspect_http_exchange.py
import gzip
from threading import Thread
from urllib.parse import parse_qs, urlsplit

from bs4 import BeautifulSoup
from flask import Flask, Response, jsonify, request
import requests
from werkzeug.serving import make_server, WSGIRequestHandler


app = Flask(__name__)


@app.get("/notice")
def notice():
    html = "<!doctype html><title>Water &amp; light</title><p>Check at noon.</p>"
    response = Response(gzip.compress(html.encode("utf-8")),
                        content_type="text/html; charset=utf-8")
    response.headers["Content-Encoding"] = "gzip"
    response.set_cookie("visit", "public-demo", path="/")
    return response


@app.post("/inspect")
def inspect():
    return jsonify(query=request.args.to_dict(flat=False),
                   body=request.get_json(),
                   cookie_seen=request.cookies.get("visit"),
                   client=request.headers.get("X-Demo-Client"))


class QuietHandler(WSGIRequestHandler):
    def log_request(self, *args, **kwargs):
        pass


def main():
    server = make_server("127.0.0.1", 0, app, request_handler=QuietHandler)
    thread = Thread(target=server.serve_forever)
    thread.start()
    try:
        base = f"http://127.0.0.1:{server.server_port}"
        with requests.Session() as session:
            with session.get(base + "/notice", timeout=(2, 3)) as response:
                response.raise_for_status()
                print(response.status_code, response.reason)
                print(response.headers["content-type"])
                print(response.headers["Content-Encoding"])
                soup = BeautifulSoup(response.text, "html.parser")
                print(soup.title.get_text())
                print(response.cookies.get("visit"))
                try:
                    response.json()
                except requests.exceptions.JSONDecodeError:
                    print("HTML is not JSON")

            query = {"group": ["north hall", "south&west"], "page": 2}
            body = {"sample": {"labels": ["shade", "sun"], "reading": None}}
            with session.post(base + "/inspect", params=query, json=body,
                              headers={"X-Demo-Client": "field-notebook"},
                              timeout=(2, 3)) as response:
                response.raise_for_status()
                assert response.status_code == 200
                assert response.headers["Content-Type"].split(";")[0] == "application/json"
                received = response.json()
                assert received["query"] == {
                    "group": ["north hall", "south&west"], "page": ["2"]}
                assert parse_qs(urlsplit(response.url).query) == received["query"]
                assert received["body"] == body
                assert received["cookie_seen"] == "public-demo"
                assert received["client"] == "field-notebook"
                print("query, JSON, header and session cookie arrived")

            with session.get(base + "/missing", timeout=(2, 3)) as response:
                print("response received:", response.status_code)
                try:
                    response.raise_for_status()
                except requests.HTTPError:
                    print("status check raised HTTPError")
    finally:
        server.shutdown()
        thread.join()
        server.server_close()


if __name__ == "__main__":
    main()
