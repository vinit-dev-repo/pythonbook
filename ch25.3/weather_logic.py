# weather_logic.py
def get_weather(weather_service):
    data = weather_service.fetch("London")
    return f"It is {data['temp']}°C in London"
