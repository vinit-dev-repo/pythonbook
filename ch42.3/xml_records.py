# xml_records.py
from io import BytesIO
import xml.etree.ElementTree as ET

document = (
    b'<?xml version="1.0" encoding="iso-8859-1"?>'
    b'<route><stop code="N"><name>Rivi\xe8re &amp; Parc</name></stop>'
    b'<stop code="S"><name>South <em>Gate</em></name></stop></route>'
)
root = ET.fromstring(document)
for stop in root.findall("stop"):
    name = stop.find("name")
    if name is None:
        raise ValueError("A stop needs a name element")
    print(stop.get("code"), "".join(name.itertext()))
print("Immediate text:", repr(root.find("stop[@code='S']/name").text))
print("Missing:", root.find("missing") is None)
encoded = ET.tostring(root, encoding="utf-8", xml_declaration=True)
again = ET.parse(BytesIO(encoded)).getroot()
print(type(encoded).__name__, type(again.find("stop/name").text).__name__)
print("Same first name:", again.find("stop/name").text == root.find("stop/name").text)
try:
    ET.fromstring(b"<route><stop></route>")
except ET.ParseError:
    print("Broken nesting rejected")
