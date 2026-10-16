import requests

try:
    response = requests.get("https://api.github.com/users/does-not-exist-xyz", timeout=5)
    response.raise_for_status()   # raises an error if status is 4xx or 5xx
    print(response.json())
except requests.exceptions.HTTPError as error:
    print(f"The API said no: {error}")
except requests.exceptions.Timeout:
    print("Timed out while waiting for the connection or response data.")
except requests.exceptions.RequestException as error:
    print(f"Something went wrong: {error}")
