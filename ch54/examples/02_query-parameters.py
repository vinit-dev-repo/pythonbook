import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python stars:>10000", "sort": "stars"},
    timeout=5,
)
response.raise_for_status()   # apply the status check learned in B2
data = response.json()
print(response.url)
# A successful response can still lack an expected field.
print(data.get("total_count", "count unavailable"))
