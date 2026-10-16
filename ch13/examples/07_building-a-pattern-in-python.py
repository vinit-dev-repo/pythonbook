import re

date_pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
match = date_pattern.fullmatch("2026-08-24")

print(match.group("year"))
print(match.groupdict())
