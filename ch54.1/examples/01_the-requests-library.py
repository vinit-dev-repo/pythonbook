import requests

response = requests.get("https://api.github.com/users/python", timeout=5)
print(response.status_code)
print(response.ok)
data = response.json()
# A missing field does not tell us why it is absent.
# These defaults describe the data, not the cause of an HTTP failure.
print(data.get("name", "name unavailable"), data.get("public_repos", "count unavailable"))
