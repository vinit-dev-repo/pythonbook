import json
import shelve
import tempfile
import xml.etree.ElementTree as ET
from decimal import Decimal
from pathlib import Path

import yaml

# 1
with tempfile.TemporaryDirectory() as folder:
    name = str(Path(folder) / "settings")
    with shelve.open(name) as db:
        db["recent"] = ["a", "b"]
    with shelve.open(name) as db:
        print(db["recent"], "recent" in db)

# 2
settings = yaml.safe_load("name: Amy\nscores:\n  - 90\n  - 85\n")
print(settings)
try:
    yaml.safe_load("value: !!python/object/apply:os.getcwd []")
except yaml.YAMLError:
    print("safe_load refused the Python tag")

# 3
root = ET.fromstring('<route><stop code="A1"><name>East Park</name></stop><stop code="B2"><name>Dock</name></stop></route>')
for stop in root.findall("stop"):
    print(stop.get("code"), stop.find("name").text)


# 4
def encode(value):
    if isinstance(value, Decimal):
        return {"$decimal": str(value)}
    raise TypeError(type(value))


def decode(d):
    if "$decimal" in d:
        return Decimal(d["$decimal"])
    return d


text = json.dumps({"waste": Decimal("0.0001")}, default=encode)
back = json.loads(text, object_hook=decode)
print(text)
print(back["waste"], back["waste"].as_tuple().exponent)
