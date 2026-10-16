import re

text = "Order 12 apples, 5 bananas and 100 grapes."

print(re.findall(r"\d+", text))
