# test_document_cache.py
import json
import subprocess
import sys
import threading
import unittest
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from document_cache import load_document

@contextmanager
def local_document():
    class Handler(BaseHTTPRequestHandler):
        reply = (200, "application/json", b'{"revision":1}')
        calls = 0
        def do_GET(self):
            type(self).calls += 1
            status, media_type, body = type(self).reply
            self.send_response(status)
            self.send_header("Content-Type", media_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        def log_message(self, *args):
            pass

    with HTTPServer(("127.0.0.1", 0), Handler) as server:
        worker = threading.Thread(target=server.serve_forever)
        worker.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}/document", Handler
        finally:
            server.shutdown()
            worker.join()

class CacheTests(unittest.TestCase):
    def test_persistence_refresh_and_failure(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "saved.json"
            with local_document() as (url, handler):
                first = load_document(url, path)
                first["revision"] = 99
                self.assertEqual(load_document(url, path), {"revision": 1})
                self.assertEqual(handler.calls, 1)
                handler.reply = (200, "application/json", b'{"revision":2}')
                self.assertEqual(load_document(url, path, refresh=True),
                                 {"revision": 2})
                saved = path.read_bytes()
                for reply in [
                    (503, "application/json", b'{}'),
                    (302, "application/json", b'{}'),
                    (200, "text/plain", b'{}'),
                    (200, "application/json", b'{'),
                    (200, "application/json", b'[]'),
                    (200, "application/json", b' ' * 65537),
                ]:
                    handler.reply = reply
                    with self.subTest(reply=reply[:2]):
                        with self.assertRaises(ValueError):
                            load_document(url, path, refresh=True)
                        self.assertEqual(path.read_bytes(), saved)
                count = handler.calls
                with self.assertRaises(ValueError):
                    load_document(url + "-other", path)
                self.assertEqual(handler.calls, count)
                path.write_text("{", encoding="utf8")
                with self.assertRaises(ValueError):
                    load_document(url, path)
                self.assertEqual(handler.calls, count)
                handler.reply = (200, "application/json", b'{"revision":2}')
                load_document(url, path, refresh=True)
                self.assertEqual(list(Path(folder).glob("document-*.tmp")), [])
            command = [sys.executable, "-c",
                       "import sys; from document_cache import load_document; "
                       "print(load_document(sys.argv[1], sys.argv[2]))", url, str(path)]
            result = subprocess.run(command, capture_output=True, text=True,
                                    timeout=10, cwd=Path(__file__).parent)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), "{'revision': 2}")

if __name__ == "__main__":
    unittest.main()
