import re

print(ascii(re.findall(r"\w+", "café")))
print(re.findall(rb"\w+", "café".encode("utf-8")))

try:
    re.search(rb"caf", "café")
except TypeError as error:
    print(type(error).__name__)
