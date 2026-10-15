# document_cache.py
import json
from pathlib import Path
from tempfile import NamedTemporaryFile
import requests

def object_document(data):
    document = json.loads(data)
    if not isinstance(document, dict):
        raise ValueError("document must be a JSON object")
    return document

def load_document(url, cache_path, *, refresh=False):
    path = Path(cache_path)
    if not refresh:
        try:
            envelope = object_document(path.read_text(encoding="utf8"))
        except FileNotFoundError:
            pass
        else:
            if envelope.get("url") != url:
                raise ValueError("cache belongs to another URL")
            document = envelope.get("document")
            if not isinstance(document, dict):
                raise ValueError("cache contains an invalid document")
            return document

    with requests.get(url, timeout=(2, 3), stream=True,
                      allow_redirects=False) as response:
        if response.status_code != 200:
            raise ValueError(f"expected HTTP 200, got {response.status_code}")
        media_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
        if media_type != "application/json":
            raise ValueError("expected application/json")
        data = bytearray()
        for chunk in response.iter_content(chunk_size=4096):
            data.extend(chunk)
            if len(data) > 65536:
                raise ValueError("document exceeds this lab's size limit")
    document = object_document(data.decode("utf8"))
    encoded = json.dumps({"url": url, "document": document}, ensure_ascii=False)
    temporary = None
    try:
        with NamedTemporaryFile(mode="w", encoding="utf8", dir=path.parent,
                                prefix="document-", suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(encoded)
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return document
