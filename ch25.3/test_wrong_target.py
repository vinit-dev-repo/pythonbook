# test_wrong_target.py
from unittest.mock import patch
import weather_report

def test_wrong_patch_target():
    with patch("weather_source.fetch", return_value={"temp": 18}):
        assert weather_report.london_report() == "It is 18°C in London"
