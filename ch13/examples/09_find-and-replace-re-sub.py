import re

text = "Smith, John\nDoe, Jane"
reordered = re.sub(r"(\w+), (\w+)", r"\2 \1", text)
print(reordered)
