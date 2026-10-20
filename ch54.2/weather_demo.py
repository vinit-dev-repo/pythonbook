# weather_demo.py
from requests import ConnectionError

from test_weather_client import FakeResponse, FakeSession, captured, payload
from weather_client import ENDPOINT, WeatherReport, get_weather


def run_demo():
    environ = {"WEATHER_API_KEY": "public-test-key-A"}
    good = FakeSession(FakeResponse(payload=payload("Oslo", 4, "snow")))
    observed = captured(
        lambda: get_weather("Oslo", session=good, environ=environ)
    )
    assert observed == (WeatherReport("Oslo", 4.0, "snow"), "", "")
    assert good.calls == [
        (
            ENDPOINT,
            {"q": "Oslo"},
            {"X-API-Key": "public-test-key-A"},
            (3, 10),
            False,
        )
    ]

    malformed = payload("Oslo", "public-test-key-B", "snow")
    bad = FakeSession(FakeResponse(payload=malformed))
    observed = captured(
        lambda: get_weather("Oslo", session=bad, environ=environ)
    )
    assert observed == (None, "weather: invalid response\n", "")
    assert len(bad.calls) == 1

    offline = FakeSession(ConnectionError("public-test-key-A"))
    observed = captured(
        lambda: get_weather("Oslo", session=offline, environ=environ)
    )
    assert observed == (None, "weather: transport\n", "")
    assert len(offline.calls) == 1
    print("offline weather transfer: ok")


if __name__ == "__main__":
    run_demo()
