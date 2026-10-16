import re

text = "Order 12 apples, 5 bananas and 100 grapes."

for match in re.finditer(r"\d+", text):
    print(match.group(), "at position", match.start())
