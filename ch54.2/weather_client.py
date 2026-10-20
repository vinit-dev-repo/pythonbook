# weather_client.py
from dataclasses import dataclass
import math
import os

import requests


ENDPOINT = "https://weather.example.invalid/v1/current"


@dataclass
class WeatherReport:
    city: str
    temperature_c: float
    description: str


def load_api_key(environ: dict[str, object]) -> str:
    key = environ.get("WEATHER_API_KEY")
    if (
        not isinstance(key, str)
        or not key
        or not key.isascii()
        or not key.isprintable()
        or any(character.isspace() for character in key)
    ):
        raise ValueError("WEATHER_API_KEY is invalid")
    return key


def _city(city: object) -> str:
    if not isinstance(city, str) or not city.strip():
        raise ValueError("city must be a nonblank string")
    return city.strip()


def _invalid_response() -> None:
    print("weather: invalid response")


def get_weather(city: str, *, session=requests, environ=None) -> WeatherReport | None:
    clean_city = _city(city)
    if environ is None:
        environ = os.environ
    try:
        key = load_api_key(environ)
    except ValueError:
        print("weather: configuration failed")
        return None

    try:
        response = session.get(
            ENDPOINT,
            params={"q": clean_city},
            headers={"X-API-Key": key},
            timeout=(3, 10),
            allow_redirects=False,
        )
    except requests.exceptions.Timeout:
        print("weather: timeout")
        return None
    except requests.exceptions.RequestException:
        print("weather: transport")
        return None

    if response.status_code != 200:
        print("weather: unexpected HTTP status")
        return None
    try:
        data = response.json()
    except (requests.exceptions.JSONDecodeError, ValueError, TypeError):
        _invalid_response()
        return None
    try:
        name = data["location"]["name"]
        description = data["current"]["condition"]["text"]
        raw_temperature = data["current"]["temp_c"]
        if (
            not isinstance(name, str)
            or not name
            or not isinstance(description, str)
            or not description
            or isinstance(raw_temperature, bool)
        ):
            raise ValueError
        temperature_c = float(raw_temperature)
        if not math.isfinite(temperature_c):
            raise ValueError
    except (KeyError, TypeError, ValueError, OverflowError):
        _invalid_response()
        return None
    return WeatherReport(name, temperature_c, description)
