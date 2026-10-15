# exercise_http_resources.py
from requests.exceptions import ConnectTimeout
from http_resources import BASE_URL, ResponseTooLarge, read_resource
from test_http_resources import FakeResponse, FakeSession, assert_calls


def run_exercise():
    events, sleeps = [], []
    beta = FakeResponse(200, [b"xy", b"z"], events=events, label="beta")
    alpha = FakeResponse(200, [b"12", b"345", b"unread"], events=events, label="alpha")
    session = FakeSession([ConnectTimeout(), beta, alpha], events)

    def sleep(delay):
        sleeps.append(delay)
        events.append(("sleep", delay))

    try:
        with session:
            assert read_resource("beta", session=session, max_bytes=4,
                                 sleep=sleep) == b"xyz"
            read_resource("alpha", session=session, max_bytes=4, sleep=sleep)
    except ResponseTooLarge:
        pass
    else:
        raise AssertionError("alpha should exceed four bytes")
    assert_calls(session, ["beta", "beta", "alpha"])
    assert sleeps == [0.25] and alpha.read_count == 2
    assert events == [
        ("session", "enter"), ("get", f"{BASE_URL}/beta"),
        ("sleep", 0.25), ("get", f"{BASE_URL}/beta"),
        ("beta", "enter"), ("beta", "chunk", b"xy"), ("beta", "chunk", b"z"),
        ("beta", "close", None), ("get", f"{BASE_URL}/alpha"),
        ("alpha", "enter"), ("alpha", "chunk", b"12"), ("alpha", "chunk", b"345"),
        ("alpha", "close", "ResponseTooLarge"),
        ("session", "close", "ResponseTooLarge"),
    ]
    print("manual session: ok")


if __name__ == "__main__":
    run_exercise()
