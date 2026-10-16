import requests

response = requests.get("https://quotes.toscrape.com/", timeout=5)
print(response.status_code)
print("<title>Quotes to Scrape</title>" in response.text)
print(response.text.lstrip().startswith("<!DOCTYPE html>"))
