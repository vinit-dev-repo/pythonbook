from dataclasses import dataclass

@dataclass
class Draft:
    title: str

@dataclass(frozen=True)
class Stamp:
    code: str
    revision: int

@dataclass(frozen=True)
class FrozenNotes:
    title: str
    tags: list[str]

notes = FrozenNotes("Guide", [])
try:
    notes.title = "New guide"
except AttributeError as error:
    print("field replacement:", type(error).__name__)
notes.tags.append("python")
print("nested mutation:", notes.tags)

for label, value in (("draft", Draft("Guide")), ("stamp", Stamp("A", 1)), ("notes", notes)):
    try:
        result = len({value, Stamp("A", 1)}) if label == "stamp" else len({value})
        print(label, "set size:", result)
    except TypeError as error:
        print(label, "hash use:", type(error).__name__)
