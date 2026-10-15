# row_demo.py
from record_rows import rows_to_records

rows = [
    {"name": "Ada", "score": 10},
    {"score": 20, "team": "blue", "name": "Grace"},
    {"team": "green", "name": "Lin"},
]
records = rows_to_records(rows)

print("fields:", records[0]._fields)
print("first:", records[0])
print("second score:", records[1].score)
print("third missing score:", records[2].score)
print("input order:", [record.name for record in records])
print("shared class:", records[0].__class__ is records[2].__class__)
print("empty:", rows_to_records([]))
