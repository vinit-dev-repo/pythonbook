import requests

response = requests.post("http://127.0.0.1:5000/todos", json={"task": "Try the API"}, timeout=5)
print(response.status_code)
print(response.json())

response = requests.get("http://127.0.0.1:5000/todos", timeout=5)
print(response.json())
