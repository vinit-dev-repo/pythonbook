from collections import namedtuple
from dataclasses import FrozenInstanceError, dataclass


# 1
@dataclass(frozen=True)
class Pin:
    code: str
    tags: list[str]


pin = Pin("A1", [])
try:
    pin.code = "B2"
except FrozenInstanceError as error:
    print(type(error).__name__)
pin.tags.append("new")
print(pin.tags)
try:
    print(len({pin}))
except TypeError as error:
    print(type(error).__name__)


# 2
rows = [{"b": 1}, {"a": 2, "b": 3}]
names = sorted({name for row in rows for name in row})
Row = namedtuple("Row", names, defaults=(None,) * len(names))
records = [Row(**row) for row in rows]
print(Row._fields)
print(records)
