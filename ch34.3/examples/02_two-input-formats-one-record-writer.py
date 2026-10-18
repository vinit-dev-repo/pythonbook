import csv
import io
import json

def csv_records(lines):
    for row in csv.DictReader(lines):
        yield {"name": row["name"], "quantity": int(row["quantity"])}

def json_records(lines):
    for line in lines:
        if line.strip():
            yield json.loads(line)

def write_records(records, destination):
    written = 0
    for record in records:
        name, quantity = record["name"], record["quantity"]
        if type(name) is not str or not name:
            raise ValueError("name must be a nonempty string")
        if type(quantity) is not int or quantity < 0:
            raise ValueError("quantity must be a nonnegative integer")
        normalized = {"name": name, "quantity": quantity}
        destination.write(json.dumps(normalized, ensure_ascii=False) + "\n")
        written += 1
    return written

csv_source = io.StringIO("name,quantity\nbolts,3\nwashers,0\n")
json_source = io.StringIO(
    '{"quantity": 3, "name": "bolts"}\n'
    '{"name": "washers", "quantity": 0}\n'
)
for label, reader, source in (
    ("csv", csv_records, csv_source),
    ("json", json_records, json_source),
):
    output = io.StringIO()
    count = write_records(reader(source), output)
    print(label, count, output.getvalue().splitlines())

output = io.StringIO()
source = io.StringIO("name,quantity\nbolts,3\nwashers,invalid\nspacers,4\n")
try:
    write_records(csv_records(source), output)
except ValueError:
    print("failed after:", output.getvalue().splitlines())
print("unread:", source.readline().strip())
