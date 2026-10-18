# weather_report.py
from weather_source import fetch

def london_report():
    data = fetch("London")
    return f"It is {data['temp']}°C in London"
