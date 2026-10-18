# row_transfer.py
from record_rows import rows_to_records

shared = []
records = rows_to_records([{'score': 8, 'tags': shared}, {'name': 'Mina'}])
print(records[0])
print(records[1])
shared.append('new')
print(shared)
print(records[0].tags)
