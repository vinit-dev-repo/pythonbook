from dataclasses import dataclass, field

try:
    @dataclass
    class BrokenNotebook:
        pages: list[str] = []
except ValueError as error:
    print("definition failure:", type(error).__name__)

@dataclass
class Notebook:
    title: str
    edition: int = 1
    pages: list[str] = field(default_factory=list)

first = Notebook("Ideas")
second = Notebook("Plans")
keyword = Notebook(title="Archive", edition=2)
print("same factory list:", first.pages is second.pages)
first.pages.append("sketch")

print("scalar default:", first.edition)
print("keyword construction:", keyword.title, keyword.edition)
print("states:", first.pages, second.pages)
