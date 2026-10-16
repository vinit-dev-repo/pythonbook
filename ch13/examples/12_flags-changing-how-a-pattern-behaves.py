import re

text = "line one\nline two\nline three"
print(re.findall(r"^line \w+", text, re.MULTILINE))
