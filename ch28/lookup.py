# lookup.py
from record_rows import rows_to_records

source = {"name": "Ada", "score": 10}
record = rows_to_records([source])[0]
field_name = "score"
print(record.name)
print(source.get(field_name))
print(getattr(record, field_name, None))
print(getattr(record, "team", None))
