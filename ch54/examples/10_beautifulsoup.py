from bs4 import BeautifulSoup

html = """
<div class="quote">
    <span class="text">"Simplicity is the soul of efficiency."</span>
    <small class="author">Austin Freeman</small>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

quote = soup.find("span", class_="text")
author = soup.find("small", class_="author")
print(quote.text)
print(author.text)
