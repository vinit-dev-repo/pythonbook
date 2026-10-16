import re

# 1
print(re.findall(r"\b[A-Z]\w*", "My Name is Vinit and I live in Delhi"))
# ['My', 'Name', 'Vinit', 'I', 'Delhi']

# 2
print(re.sub(r"\d+", "NUMBER", "Room 12B, Room 004, Room 7"))
# Room NUMBERB, Room NUMBER, Room NUMBER

# 3
match = re.search(r"(?P<year>\d{4})", "23-Aug-2026")
print(match.group("year"))
# 2026

# 4
print(re.search(r"a.*b", "a123b456b").group())    # a123b456b  (greedy: goes to the LAST b)
print(re.search(r"a.*?b", "a123b456b").group())   # a123b     (lazy: stops at the FIRST b)

# 5
postcode_pattern = re.compile(r"""
    ^[A-Z]{1,2}   # one or two letters (area)
    [0-9][A-Z0-9]? # ASCII digit, then an optional ASCII letter or digit
    [ ]           # one space
    [0-9]         # one ASCII digit (sector)
    [A-Z]{2}$     # two letters (unit)
""", re.VERBOSE)
print(bool(postcode_pattern.fullmatch("SW1A 1AA")))
# True
