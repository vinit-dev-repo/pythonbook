from typing import Protocol, runtime_checkable

@runtime_checkable
class Report(Protocol):
    def render(self, rows): ...

class CsvReport:
    def render(self, rows):
        return "\n".join(",".join(str(c) for c in r) for r in rows)

class TextReport:
    def render(self, rows):
        return "\n".join(" | ".join(str(c) for c in r) for r in rows)

class SomeoneElsesReport:            # not ours, never edited
    def render(self, rows):
        return f"<{len(rows)} rows>"

def print_all(reports, rows):
    for r in reports:
        print(r.render(rows))

print_all([CsvReport(), TextReport(), SomeoneElsesReport()], [[1, "a"], [2, "b"]])
print(isinstance(SomeoneElsesReport(), Report))

from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Row:
    quantity: int
    label: str

class Format(Enum):
    CSV = "csv"
    TEXT = "text"

renderers = {Format.CSV: CsvReport(), Format.TEXT: TextReport()}
records = [Row(1, "a"), Row(2, "b")]
cells = [[row.quantity, row.label] for row in records]
print(renderers[Format.CSV].render(cells))
