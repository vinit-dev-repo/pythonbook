# test_http_resources.py
from requests.exceptions import (
    ConnectTimeout, ConnectionError, ContentDecodingError, ReadTimeout, SSLError,
)
from http_resources import (
    BASE_URL, ResponseTooLarge, UnexpectedStatus, load_pair, read_resource,
)


def error_name(kind):
    return None if kind is None else kind.__name__


class FakeResponse:
    def __init__(self, status, chunks=(), *, events=None, label="response", headers=None):
        self.status_code = status
        self.chunks = list(chunks)
        self.events = [] if events is None else events
        self.label = label
        self.headers = {} if headers is None else headers
        self.read_count = 0

    def __enter__(self):
        self.events.append((self.label, "enter"))
        return self

    def __exit__(self, kind, value, traceback):
        self.events.append((self.label, "close", error_name(kind)))

    def iter_content(self, *, chunk_size):
        assert chunk_size == 256
        for item in self.chunks:
            self.read_count += 1
            if isinstance(item, BaseException):
                self.events.append((self.label, "stream-error", type(item).__name__))
                raise item
            self.events.append((self.label, "chunk", item))
            yield item

    @property
    def content(self):
        raise AssertionError("eager content access")

    @property
    def text(self):
        raise AssertionError("eager text access")

    def json(self):
        raise AssertionError("eager json access")


class FakeSession:
    def __init__(self, outcomes, events=None):
        self.outcomes = list(outcomes)
        self.events = [] if events is None else events
        self.calls = []

    def __enter__(self):
        self.events.append(("session", "enter"))
        return self

    def __exit__(self, kind, value, traceback):
        self.events.append(("session", "close", error_name(kind)))

    def get(self, url, *, stream, timeout, allow_redirects):
        self.calls.append((url, stream, timeout, allow_redirects))
        self.events.append(("get", url))
        item = self.outcomes.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item


def raises(kind, call):
    try:
        call()
    except kind as error:
        return error
    raise AssertionError(f"{kind.__name__} was required")


def assert_calls(session, names):
    assert session.calls == [
        (f"{BASE_URL}/{name}", True, (3, 10), False) for name in names
    ], session.calls


def assert_close_before_retry(events):
    # Check the FIRST sleep and next get, not any convenient later sleep.
    assert events[:5] == [
        ("get", f"{BASE_URL}/alpha"),
        ("r503", "enter"),
        ("r503", "close", None),
        ("sleep", 0.25),
        ("get", f"{BASE_URL}/alpha"),
    ], events


def faulty_read_resource_without_response_context(session, sleep):
    # A real faulty two-attempt operation: it never closes either response.
    response = session.get(
        f"{BASE_URL}/alpha", stream=True, timeout=(3, 10), allow_redirects=False,
    )
    if response.status_code == 503:
        sleep(0.25)
        response = session.get(
            f"{BASE_URL}/alpha", stream=True, timeout=(3, 10), allow_redirects=False,
        )
    return b"".join(response.iter_content(chunk_size=256))


def check_inputs():
    for value, kind in ((None, TypeError), (1, TypeError), ([], TypeError),
                        ("wrong", ValueError), ("", ValueError)):
        session = FakeSession([])
        raises(kind, lambda: read_resource(value, session=session))
        assert not session.calls

    class IntChild(int):
        pass

    invalid = [(True, TypeError), (False, TypeError), (1.0, TypeError),
               ("1", TypeError), (IntChild(1), TypeError),
               (0, ValueError), (-1, ValueError)]
    for value, kind in invalid:
        opened = []
        raises(kind, lambda: load_pair(
            session_factory=lambda: opened.append("opened"), max_bytes=value,
        ))
        assert opened == []
        session = FakeSession([])
        raises(kind, lambda: read_resource("alpha", session=session, max_bytes=value))
        assert session.calls == []


def check_bodies_and_terminal_failures():
    for chunks, expected, headers in (
        ([], b"", {}), ([b""], b"", {}),
        ([b"ab", b"", b"cd"], b"abcd", {"Content-Length": "999999"}),
    ):
        events, sleeps = [], []
        response = FakeResponse(200, chunks, events=events, headers=headers)
        session = FakeSession([response], events)
        assert read_resource("alpha", session=session, max_bytes=4,
                             sleep=sleeps.append) == expected
        assert_calls(session, ["alpha"])
        assert sleeps == []
        assert events[-1] == ("response", "close", None)
        assert not any(event[0] == "session" for event in events)

    for status in (201, 204, 302, 400, 429, 500):
        events, sleeps = [], []
        response = FakeResponse(status, [b"unread"], events=events)
        session = FakeSession([response], events)
        error = raises(UnexpectedStatus, lambda: read_resource(
            "alpha", session=session, sleep=sleeps.append,
        ))
        assert error.status == status
        assert_calls(session, ["alpha"])
        assert sleeps == [] and response.read_count == 0
        assert events == [("get", f"{BASE_URL}/alpha"), ("response", "enter"),
                          ("response", "close", "UnexpectedStatus")]

    for error in (ReadTimeout("read"), ConnectionError("connection"), SSLError("tls")):
        session, sleeps = FakeSession([error]), []
        assert raises(type(error), lambda: read_resource(
            "alpha", session=session, sleep=sleeps.append,
        )) is error
        assert_calls(session, ["alpha"])
        assert sleeps == []
        assert session.events == [("get", f"{BASE_URL}/alpha")]

    for error in (ReadTimeout("read"), ConnectTimeout("stream-connect"),
                  ContentDecodingError("decode"), RuntimeError("stream")):
        events, sleeps = [], []
        response = FakeResponse(200, [b"ok", error, b"unread"], events=events)
        session = FakeSession([response], events)
        assert raises(type(error), lambda: read_resource(
            "alpha", session=session, sleep=sleeps.append,
        )) is error
        assert_calls(session, ["alpha"])
        assert sleeps == [] and response.read_count == 2
        assert events[-1] == ("response", "close", type(error).__name__)

    events, sleeps = [], []
    response = FakeResponse(200, [b"ab", b"c", b"unread"], events=events,
                            headers={"Content-Length": "0"})
    session = FakeSession([response], events)
    raises(ResponseTooLarge, lambda: read_resource(
        "alpha", session=session, max_bytes=2, sleep=sleeps.append,
    ))
    assert_calls(session, ["alpha"])
    assert sleeps == [] and response.read_count == 2
    assert events[-1] == ("response", "close", "ResponseTooLarge")


def check_retries():
    events, sleeps = [], []
    rejected = FakeResponse(503, [b"unread"], events=events, label="r503")
    accepted = FakeResponse(200, [b"ok"], events=events, label="r200")
    session = FakeSession([ConnectTimeout(), rejected, accepted], events)

    def sleep(delay):
        events.append(("sleep", delay))
        sleeps.append(delay)

    assert read_resource("alpha", session=session, sleep=sleep) == b"ok"
    assert_calls(session, ["alpha"] * 3)
    assert sleeps == [0.25, 0.5] and rejected.read_count == 0
    assert events == [
        ("get", f"{BASE_URL}/alpha"), ("sleep", 0.25),
        ("get", f"{BASE_URL}/alpha"), ("r503", "enter"),
        ("r503", "close", None), ("sleep", 0.5),
        ("get", f"{BASE_URL}/alpha"), ("r200", "enter"),
        ("r200", "chunk", b"ok"), ("r200", "close", None),
    ]

    for failure in ("status", "connect"):
        events, sleeps = [], []
        outcomes = [FakeResponse(503, [b"unread"], events=events, label=str(i))
                    if failure == "status" else ConnectTimeout(str(i))
                    for i in range(3)]
        session = FakeSession(outcomes, events)
        kind = UnexpectedStatus if failure == "status" else ConnectTimeout
        error = raises(kind, lambda: read_resource(
            "alpha", session=session, sleep=sleeps.append,
        ))
        assert_calls(session, ["alpha"] * 3)
        assert sleeps == [0.25, 0.5]
        if failure == "status":
            assert error.status == 503
            assert [event for event in events if event[1] == "close"] == [
                (str(i), "close", None) for i in range(3)
            ]
            assert all(response.read_count == 0 for response in outcomes)
        else:
            assert error is outcomes[-1]
            assert len(events) == 3

    for faulty in (False, True):
        events = []
        session = FakeSession([
            FakeResponse(503, events=events, label="r503"),
            FakeResponse(200, [b"ok"], events=events, label="r200"),
        ], events)
        sleep = lambda delay: events.append(("sleep", delay))
        if faulty:
            assert faulty_read_resource_without_response_context(session, sleep) == b"ok"
            faulty_events = events
            raises(AssertionError, lambda: assert_close_before_retry(faulty_events))
        else:
            assert read_resource("alpha", session=session, sleep=sleep) == b"ok"
            assert_close_before_retry(events)


def check_pair():
    events, opened, sleeps = [], [], []
    alpha = FakeResponse(200, [b"aaaa"], events=events, label="alpha")
    beta = FakeResponse(200, [b"bbbb"], events=events, label="beta")
    session = FakeSession([alpha, beta], events)

    def factory():
        opened.append(session)
        return session

    assert load_pair(session_factory=factory, max_bytes=4,
                     sleep=sleeps.append) == (b"aaaa", b"bbbb")
    assert opened == [session] and sleeps == []
    assert_calls(session, ["alpha", "beta"])
    assert events == [
        ("session", "enter"), ("get", f"{BASE_URL}/alpha"),
        ("alpha", "enter"), ("alpha", "chunk", b"aaaa"), ("alpha", "close", None),
        ("get", f"{BASE_URL}/beta"), ("beta", "enter"),
        ("beta", "chunk", b"bbbb"), ("beta", "close", None),
        ("session", "close", None),
    ]

    for first_fails in (True, False):
        events, opened, sleeps, returned = [], [], [], []
        alpha = FakeResponse(500 if first_fails else 200, [b"a"], events=events,
                             label="alpha")
        beta = FakeResponse(500, [b"unread"], events=events, label="beta")
        session = FakeSession([alpha, beta], events)

        def factory():
            opened.append(session)
            return session

        def operation():
            returned.append(load_pair(session_factory=factory, sleep=sleeps.append))

        assert raises(UnexpectedStatus, operation).status == 500
        assert opened == [session] and returned == [] and sleeps == []
        assert_calls(session, ["alpha"] if first_fails else ["alpha", "beta"])
        assert events[-1] == ("session", "close", "UnexpectedStatus")
        assert ("alpha", "close", "UnexpectedStatus" if first_fails else None) in events
        assert beta.read_count == 0
        if not first_fails:
            assert events[-2] == ("beta", "close", "UnexpectedStatus")

    # Each resource starts a fresh attempt budget.
    sleeps = []
    session = FakeSession([ConnectTimeout(), ConnectTimeout(), FakeResponse(200),
                           ConnectTimeout(), ConnectTimeout(), FakeResponse(200)])
    assert load_pair(session_factory=lambda: session, sleep=sleeps.append) == (b"", b"")
    assert_calls(session, ["alpha"] * 3 + ["beta"] * 3)
    assert sleeps == [0.25, 0.5, 0.25, 0.5]


def run_checks():
    check_inputs()
    check_bodies_and_terminal_failures()
    check_retries()
    check_pair()
    print("http resource checks: ok")


if __name__ == "__main__":
    run_checks()
