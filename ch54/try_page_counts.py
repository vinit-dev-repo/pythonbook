# try_page_counts.py
"""Run the page collector against a short-lived local HTTP fixture."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import urlsplit
from threaded_page_counts import collect_counts


PAGES = {
    "/board": "<p>Gate <b>seven</b></p><p>Open</p>",
    "/notice": "<h1>Café</h1><p>Meet at 9</p>",
    "/empty": "<main></main>",
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = PAGES.get(self.path)
        body = ("missing" if page is None else page).encode("utf-8")
        self.send_response(404 if page is None else 200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def main():
    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        server.daemon_threads = False
        server.block_on_close = True
        thread = Thread(target=server.serve_forever)
        thread.start()
        try:
            base = f"http://127.0.0.1:{server.server_port}"
            paths = ("/board", "/missing", "/notice", "/board", "/empty")
            results = collect_counts([base + path for path in paths])
            assert [row[1:] for row in results] == [
                (15, None), (None, "HTTP 404"), (14, None),
                (15, None), (0, None),
            ]
            for url, count, error in results:
                print(urlsplit(url).path, count if error is None else error)
        finally:
            server.shutdown()
            thread.join()


if __name__ == "__main__":
    main()
