# 28 - Record Classes, Dataclasses and Identity

The code of the chapter **28 - Record Classes, Dataclasses and Identity** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Add methods to records made with `namedtuple`.
- Compare records made with `collections.namedtuple`, `typing.NamedTuple`, and `@dataclass`.
- Use dataclass defaults and factories, and distinguish frozen fields from deeply immutable values.
- Convert dictionary rows into one consistent record schema.
- Explain why a reloaded module contains a new class object.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `record_rows.py` | Turning dictionary rows into records (line 531) |  |
| `row_demo.py` | Turning dictionary rows into records (line 554) |  |
| `lookup.py` | Turning dictionary rows into records (line 625) |  |
| `row_transfer.py` | Turning dictionary rows into records (line 653) |  |
| `shape.py` | Class identity after reloading (line 693) |  |
| `reload_check.py` | Class identity after reloading (line 719) |  |
| `saved_class_transfer.py` | Class identity after reloading (line 760) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_subclassing-to-add-behaviour.py` | Subclassing to add behaviour (line 47) | runs on its own |
| `examples/02_subclassing-to-add-behaviour.py` | Subclassing to add behaviour (line 68) | runs on its own |
| `examples/03_typing-namedtuple-tuple-behaviour-with-annotatio.py` | `typing.NamedTuple`: tuple behaviour with annotations (line 133) | may use names from earlier examples |
| `examples/04_typing-namedtuple-tuple-behaviour-with-annotatio.py` | `typing.NamedTuple`: tuple behaviour with annotations (line 156) | runs on its own |
| `examples/05_typing-namedtuple-tuple-behaviour-with-annotatio.py` | `typing.NamedTuple`: tuple behaviour with annotations (line 201) | runs on its own |
| `examples/06_dataclass-mutable-and-more-features-python-3-7.py` | `@dataclass`: mutable, and more features (Python 3.7+) (line 233) | may use names from earlier examples |
| `examples/07_dataclass-defaults-and-mutable-fields.py` | Dataclass defaults and mutable fields (line 268) | runs on its own |
| `examples/08_dataclass-defaults-and-mutable-fields.py` | Dataclass defaults and mutable fields (line 316) | runs on its own |
| `examples/09_required-keyword-only-fields-after-defaults.py` | Required keyword-only fields after defaults (line 349) | runs on its own |
| `examples/10_frozen-records-and-hashability.py` | Frozen records and hashability (line 390) | runs on its own |
| `examples/11_frozen-records-and-hashability.py` | Frozen records and hashability (line 441) | runs on its own |
| `examples/12_turning-dictionary-rows-into-records.py` | Turning dictionary rows into records (line 495) | runs on its own |
| `examples/13_turning-dictionary-rows-into-records.py` | Turning dictionary rows into records (line 596) | runs on its own |
| `examples/14_class-identity-after-reloading.py` | Class identity after reloading (line 699) | may use names from earlier examples |
| `examples/15_try-it-yourself.py` | Try it yourself (line 803) | may use names from earlier examples |
| `examples/16_try-it-yourself.py` | Try it yourself (line 815) | may use names from earlier examples |
