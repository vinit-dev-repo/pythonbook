# test_weather_report.py
from unittest.mock import patch
import weather_report
import weather_source

def test_report_uses_controlled_weather_and_restores_binding():
    original = weather_report.fetch
    with patch("weather_report.fetch", return_value={"temp": 18}) as fake_fetch:
        assert weather_report.london_report() == "It is 18°C in London"
        fake_fetch.assert_called_once_with("London")
    assert weather_report.fetch is original
    assert weather_source.fetch is original
