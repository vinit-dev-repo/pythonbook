import requests

response = requests.post(
    "https://httpbin.org/post",
    json={"title": "New Book", "pages": 320},
    headers={"User-Agent": "my-python-app/1.0"},
    timeout=5,
)
print(response.status_code)
print(response.json()["json"])
