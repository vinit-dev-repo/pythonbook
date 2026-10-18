import re

# 1
print(re.sub(r"\d+", "NUMBER", "Room 12B, Room 004, Room 7"))
# Room NUMBERB, Room NUMBER, Room NUMBER

# 2
match = re.search(r"(?P<year>\d{4})", "23-Aug-2026")
print(match.group("year"))
# 2026

# 3
print(re.sub(r"(?P<first>\w+) (?P<last>\w+)", r"\g<last>, \g<first>", "Ana Smith"))
# Smith, Ana

# 4
print(re.split(r"\s*[;,]\s*", "a;b,  c ;d"))
# ['a', 'b', 'c', 'd']
