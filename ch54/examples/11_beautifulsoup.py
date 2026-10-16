from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="/page/1">Page 1</a></li>
    <li><a href="/page/2">Page 2</a></li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
for link in soup.select("li a"):
    print(link.text, "->", link["href"])
