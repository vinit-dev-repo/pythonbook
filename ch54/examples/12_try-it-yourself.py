import requests
from dateutil import parser
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup

# 1 and 2
# The exercise asks for a friendly message when the username does not exist -
# that is a 404 and NOTHING ELSE. A 403 (rate limited), a 401 (bad token) and a
# 500 (their server broke) are different problems with different fixes, and
# calling them all "no such user" sends you hunting for a bug that is not there.
try:
    response = requests.get("https://api.github.com/users/python", timeout=5)
    response.raise_for_status()
    print(response.status_code)
    print(response.json()["public_repos"])
except requests.exceptions.HTTPError as error:
    if error.response.status_code == 404:
        print("That user does not exist.")
    else:
        print(f"GitHub returned {error.response.status_code}: {error}")

# 3
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars"},
    timeout=5
)
response.raise_for_status()          # a failed search still returns JSON, without "items"
items = response.json()["items"]
if items:                            # a search can legitimately match nothing
    print(items[0]["name"])
else:
    print("No repositories matched.")

# 4
date = parser.parse("2026-09-15")
print(date + relativedelta(months=1))
