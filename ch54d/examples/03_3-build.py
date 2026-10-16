import requests
from urllib.parse import quote

def fetch_user(username, session=requests):
    if not isinstance(username, str) or not username or username in {".", ".."}:
        raise ValueError("username must be a nonempty path segment")
    url = "https://api.example.com/users/" + quote(username, safe="")
    response = session.get(url, timeout=(3, 10))
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()

class FakeResponse:
    def __init__(self, status, payload=None, json_error=None):
        self.status_code = status
        self.payload = payload
        self.json_error = json_error
    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(str(self.status_code))
    def json(self):
        if self.json_error:
            raise self.json_error
        return self.payload

class FakeSession:
    def __init__(self, outcome):
        self.outcome = outcome
        self.calls = []
    def get(self, url, *, timeout):
        self.calls.append((url, timeout))
        if isinstance(self.outcome, BaseException):
            raise self.outcome
        return self.outcome

ok = FakeSession(FakeResponse(200, {"name": "Amara"}))
assert fetch_user("amara smith/admin", ok) == {"name": "Amara"}
assert ok.calls == [
    ("https://api.example.com/users/amara%20smith%2Fadmin", (3, 10))
]
missing = FakeSession(FakeResponse(404, json_error=AssertionError("no JSON")))
assert fetch_user("nobody", missing) is None
assert len(missing.calls) == 1
server = FakeSession(FakeResponse(500))
try:
    fetch_user("broken", server)
except requests.HTTPError as error:
    print("raised for a server error:", error)
else:
    raise AssertionError("500 must raise HTTPError")
print(fetch_user("amara smith/admin", ok))
print(fetch_user("nobody", missing))
failures = [
    ("broken", FakeResponse(500), requests.HTTPError),
    ("offline", requests.ConnectionError("offline"), requests.ConnectionError),
    ("bad-json", FakeResponse(200, json_error=ValueError("bad JSON")), ValueError),
]
for username, outcome, expected in failures:
    failed = FakeSession(outcome)
    try:
        fetch_user(username, failed)
    except Exception as error:
        assert type(error) is expected
    else:
        raise AssertionError("failure must propagate")
    assert len(failed.calls) == 1
for invalid in ("", ".", "..", 3):
    rejected = FakeSession(FakeResponse(200))
    try:
        fetch_user(invalid, rejected)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid username")
    assert rejected.calls == []
print("offline fetch_user checks: ok")
