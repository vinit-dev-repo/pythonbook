# http_resources_demo.py
from http_resources import BASE_URL, load_pair
from test_http_resources import FakeResponse, FakeSession, assert_calls


def run_demo():
    events, sleeps = [], []
    session = FakeSession([
        FakeResponse(503, events=events, label="alpha-503"),
        FakeResponse(200, [b"a", b"", b"bc"], events=events, label="alpha-200"),
        FakeResponse(200, events=events, label="beta-200"),
    ], events)

    def sleep(delay):
        sleeps.append(delay)
        events.append(("sleep", delay))

    pair = load_pair(session_factory=lambda: session, sleep=sleep)
    assert pair == (b"abc", b"") and sleeps == [0.25]
    assert_calls(session, ["alpha", "alpha", "beta"])
    assert events == [
        ("session", "enter"), ("get", f"{BASE_URL}/alpha"),
        ("alpha-503", "enter"), ("alpha-503", "close", None),
        ("sleep", 0.25), ("get", f"{BASE_URL}/alpha"),
        ("alpha-200", "enter"), ("alpha-200", "chunk", b"a"),
        ("alpha-200", "chunk", b""), ("alpha-200", "chunk", b"bc"),
        ("alpha-200", "close", None), ("get", f"{BASE_URL}/beta"),
        ("beta-200", "enter"), ("beta-200", "close", None),
        ("session", "close", None),
    ]
    print("pair:", pair)
    print("sleeps:", sleeps)


if __name__ == "__main__":
    run_demo()
