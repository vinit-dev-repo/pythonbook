from unittest.mock import Mock

def get_weather(weather_service):
    data = weather_service.fetch("London")
    return f"It is {data['temp']}°C in London"

# a fake weather_service, standing in for a real network call
fake_service = Mock()
fake_service.fetch.return_value = {"temp": 18}

print(get_weather(fake_service))
