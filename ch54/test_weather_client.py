# test_weather_client.py
import io
from contextlib import redirect_stderr, redirect_stdout

import pytest
import requests

from weather_client import ENDPOINT, WeatherReport, get_weather


class FakeResponse:
    def __init__(self, status=200, payload=None, json_error=None):
        self.status_code = status
        self.payload = payload
        self.json_error = json_error
        self.json_calls = 0

    def json(self):
        self.json_calls += 1
        if self.json_error is not None:
            raise self.json_error
        return self.payload


class FakeSession:
    def __init__(self, outcome):
        self.outcome = outcome
        self.calls = []

    def get(self, url, *, params, headers, timeout, allow_redirects):
        self.calls.append((url, params, headers, timeout, allow_redirects))
        if isinstance(self.outcome, BaseException):
            raise self.outcome
        return self.outcome


def captured(call):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        result = call()
    return result, out.getvalue(), err.getvalue()


def payload(city="Leeds", temperature=12.5, description="cloudy"):
    return {
        "location": {"name": city},
        "current": {
            "temp_c": temperature,
            "condition": {"text": description},
        },
    }


def invoke(session, *, city="Leeds", environ=None):
    if environ is None:
        environ = {"WEATHER_API_KEY": "public-test-key-A"}
    return captured(
        lambda: get_weather(city, session=session, environ=environ)
    )


@pytest.mark.parametrize("key", ["public-test-key-A", "public-test-key-B"])
def test_success_is_quiet_and_uses_the_contract(key):
    environ = {"WEATHER_API_KEY": key}
    session = FakeSession(FakeResponse(payload=payload()))
    report, out, err = invoke(session, city="  Leeds  ", environ=environ)
    assert report == WeatherReport("Leeds", 12.5, "cloudy")
    assert (out, err) == ("", "")
    assert environ == {"WEATHER_API_KEY": key}
    assert session.calls == [
        (ENDPOINT, {"q": "Leeds"}, {"X-API-Key": key}, (3, 10), False)
    ]
    url, params, headers, _, _ = session.calls[0]
    prepared = requests.Request(
        "GET", url, params=params, headers=headers
    ).prepare()
    assert key not in prepared.url
    assert prepared.headers["X-API-Key"] == key


@pytest.mark.parametrize("status", [404, 503, 302])
def test_status_is_checked_before_json(status):
    response = FakeResponse(
        status=status, json_error=AssertionError("JSON must not run")
    )
    session = FakeSession(response)
    assert invoke(session) == (
        None, "weather: unexpected HTTP status\n", ""
    )
    assert response.json_calls == 0
    assert len(session.calls) == 1


@pytest.mark.parametrize(
    "outcome,message",
    [
        (requests.Timeout("public-test-key-A"), "weather: timeout\n"),
        (requests.ConnectionError("public-test-key-B"), "weather: transport\n"),
    ],
)
def test_transport_categories_hide_exception_text(outcome, message):
    session = FakeSession(outcome)
    result, out, err = invoke(session)
    assert (result, out, err) == (None, message, "")
    assert len(session.calls) == 1
    assert "public-test-key" not in out + err


@pytest.mark.parametrize(
    "bad",
    [
        requests.exceptions.JSONDecodeError("bad public-test-key-A", "{}", 0),
        {"location": {}},
        payload(temperature="public-test-key-B"),
        payload(temperature=float("nan")),
        payload(temperature=float("inf")),
        payload(temperature=True),
    ],
)
def test_invalid_payloads_are_one_safe_category(bad):
    if isinstance(bad, BaseException):
        response = FakeResponse(json_error=bad)
    else:
        response = FakeResponse(payload=bad)
    session = FakeSession(response)
    result, out, err = invoke(session)
    assert (result, out, err) == (None, "weather: invalid response\n", "")
    assert len(session.calls) == 1
    assert "public-test-key" not in out + err


@pytest.mark.parametrize(
    "environ",
    [
        {},
        {"WEATHER_API_KEY": None},
        {"WEATHER_API_KEY": ""},
        {"WEATHER_API_KEY": "has space"},
        {"WEATHER_API_KEY": "bad\rkey"},
        {"WEATHER_API_KEY": "caf\u00e9"},
        {"WEATHER_API_KEY": 3},
    ],
)
def test_invalid_configuration_makes_no_call(environ):
    before = dict(environ)
    session = FakeSession(FakeResponse(payload=payload()))
    assert invoke(session, environ=environ) == (
        None, "weather: configuration failed\n", ""
    )
    assert session.calls == []
    assert environ == before


def test_default_environment_path_uses_only_the_dummy_key(monkeypatch):
    monkeypatch.setenv("WEATHER_API_KEY", "public-test-key-B")
    session = FakeSession(FakeResponse(payload=payload()))
    observed = captured(lambda: get_weather("Leeds", session=session))
    assert observed == (WeatherReport("Leeds", 12.5, "cloudy"), "", "")
    assert session.calls == [
        (
            ENDPOINT,
            {"q": "Leeds"},
            {"X-API-Key": "public-test-key-B"},
            (3, 10),
            False,
        )
    ]


@pytest.mark.parametrize("bad_city", [None, 3, "", "   "])
def test_invalid_city_raises_before_any_call(bad_city):
    session = FakeSession(FakeResponse(payload=payload()))
    with pytest.raises(ValueError, match="city must be a nonblank string"):
        invoke(session, city=bad_city)
    assert session.calls == []


@pytest.mark.parametrize(
    "bad_payload",
    [{}, payload(city=""), payload(description=3)],
)
def test_wrong_response_shapes_and_text_fields_are_safe(bad_payload):
    session = FakeSession(FakeResponse(payload=bad_payload))
    assert invoke(session) == (None, "weather: invalid response\n", "")
    assert len(session.calls) == 1
