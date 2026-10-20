# exercise_weather.py
from test_weather_client import FakeResponse, FakeSession, captured, payload
from weather_client import get_weather

environ = {"WEATHER_API_KEY": "public-test-key-A"}

# 1
session = FakeSession(FakeResponse(payload=payload()))
result, out, err = captured(lambda: get_weather("Leeds", session=session, environ={}))
print(result, repr(out), len(session.calls))

# 2
response = FakeResponse(503, json_error=ValueError("not JSON"))
session = FakeSession(response)
result, out, err = captured(lambda: get_weather("Leeds", session=session, environ=environ))
print(result, repr(out), response.json_calls)

# 3
for temperature in (True, float("inf")):
    session = FakeSession(FakeResponse(payload=payload(temperature=temperature)))
    result, out, err = captured(lambda: get_weather("Leeds", session=session, environ=environ))
    print(repr(temperature), result, repr(out))
