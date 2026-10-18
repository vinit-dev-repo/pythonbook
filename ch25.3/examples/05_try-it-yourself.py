from unittest.mock import Mock

def describe_temp(service, city):
    return f"{city}: {service.fetch(city)['temp']} degrees"

service = Mock()
service.fetch.return_value = {"temp": 21}
print(describe_temp(service, "Rome"))          # Rome: 21 degrees
service.fetch.assert_called_once_with("Rome")
print("call checked")                          # call checked
