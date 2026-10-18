# test_weather_logic.py
from unittest.mock import Mock
import pytest
from weather_logic import get_weather

def test_formats_the_returned_temperature():
    service = Mock()
    service.fetch.return_value = {"temp": 18}
    assert get_weather(service) == "It is 18°C in London"
    service.fetch.assert_called_once_with("London")

def test_preserves_the_dependency_error():
    service = Mock()
    failure = TimeoutError("weather unavailable")
    service.fetch.side_effect = failure
    with pytest.raises(TimeoutError) as error:
        get_weather(service)
    assert error.value is failure
    service.fetch.assert_called_once_with("London")
