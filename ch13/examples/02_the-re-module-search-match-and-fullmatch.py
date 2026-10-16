import re

text = "  hello world"
print(re.prefixmatch(r"hello", text))
print(re.prefixmatch(r"\s*hello", text))
print(re.prefixmatch is re.match)
