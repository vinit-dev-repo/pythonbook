import re

# 1
postcode_pattern = re.compile(r"""
    ^[A-Z]{1,2}   # one or two letters (area)
    [0-9][A-Z0-9]? # ASCII digit, then an optional ASCII letter or digit
    [ ]           # one space
    [0-9]         # one ASCII digit (sector)
    [A-Z]{2}$     # two letters (unit)
""", re.VERBOSE)
print(bool(postcode_pattern.fullmatch("SW1A 1AA")))
# True

# 2
print(re.findall(r"cat", "Cat CAT cat"))                  # ['cat']
print(re.findall(r"cat", "Cat CAT cat", re.IGNORECASE))   # ['Cat', 'CAT', 'cat']

# 3
digits = re.compile(r"\d+")
print(digits.findall("3 cats and 12 dogs"))   # ['3', '12']
print(digits.findall("100 sheep"))            # ['100']
