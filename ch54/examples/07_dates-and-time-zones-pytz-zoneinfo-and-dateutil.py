from dateutil import parser

print(parser.parse("23 August 2026"))
print(parser.parse("2026-08-23T15:30:00"))
print(parser.parse("Aug 23, 2026 3:30pm"))
