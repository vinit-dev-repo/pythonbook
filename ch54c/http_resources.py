# http_resources.py
import time
import requests
from requests.exceptions import ConnectTimeout

BASE_URL = "https://resources.example.invalid"
NAMES = {"alpha", "beta"}

class ResponseTooLarge(ValueError):
    pass

class UnexpectedStatus(RuntimeError):
    def __init__(self, status):
        self.status = status
        super().__init__(f"unexpected HTTP status: {status}")

def _name(name):
    if not isinstance(name, str):
        raise TypeError("name must be a str")
    if name not in NAMES:
        raise ValueError("name must be 'alpha' or 'beta'")

def _limit(max_bytes):
    if type(max_bytes) is not int:
        raise TypeError("max_bytes must be an int")
    if max_bytes <= 0:
        raise ValueError("max_bytes must be positive")

def read_resource(name, *, session, max_bytes=1024, sleep=time.sleep):
    _name(name)
    _limit(max_bytes)
    for attempt in range(3):
        try:
            response = session.get(
                f"{BASE_URL}/{name}",
                stream=True,
                timeout=(3, 10),
                allow_redirects=False,
            )
        except ConnectTimeout:
            if attempt == 2:
                raise
            sleep((0.25, 0.5)[attempt])
            continue
        retry = False
        with response:
            if response.status_code == 503:
                retry = True
            elif response.status_code != 200:
                raise UnexpectedStatus(response.status_code)
            else:
                body = bytearray()
                for chunk in response.iter_content(chunk_size=256):
                    if not chunk:
                        continue
                    if len(body) + len(chunk) > max_bytes:
                        raise ResponseTooLarge(f"body exceeds {max_bytes} bytes")
                    body.extend(chunk)
                return bytes(body)
        if attempt == 2:
            raise UnexpectedStatus(503)
        if retry:
            sleep((0.25, 0.5)[attempt])

def load_pair(*, session_factory=requests.Session, max_bytes=1024, sleep=time.sleep):
    _limit(max_bytes)
    with session_factory() as session:
        alpha = read_resource("alpha", session=session, max_bytes=max_bytes, sleep=sleep)
        beta = read_resource("beta", session=session, max_bytes=max_bytes, sleep=sleep)
        return alpha, beta
