from dataclasses import dataclass, field

@dataclass
class Notebook:
    title: str
    pages: list[str] = field(default_factory=list)

shared = []
first = Notebook("Ideas", pages=shared)
second = Notebook("Plans", pages=shared)
print(first.pages is second.pages)
first.pages.append("sketch")
print(first.pages)
print(second.pages)
