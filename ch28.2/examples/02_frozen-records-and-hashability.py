from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class TaggedNote:
    title: str
    tags: tuple[str, ...]

first = TaggedNote("Guide", ("python",))
second = TaggedNote("Guide", ("python",))
print(first is second)
print(len({first, second}))
try:
    first.tags = ("updated",)
except FrozenInstanceError as error:
    print(type(error).__name__)
print(first.tags)
