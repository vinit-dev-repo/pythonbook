import re

text = "apples, bananas,  grapes ,melons"
pieces = re.split(r"\s*,\s*", text)
print(pieces)
