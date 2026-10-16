# 19 - Tuples and Named Tuples

The code of the chapter **19 - Tuples and Named Tuples** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to use a tuple as a **record**, where each position has a meaning
- How to read a tuple with unpacking, and loop over lists of tuple-records
- Why fixed tuple slots can still lead to mutable objects, even through another tuple
- How immutability can help your program
- `namedtuple`: giving each position in a tuple a real name
- The record-editing tools: `_make`, `_asdict`, `_replace`, `_fields`, and default values

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `nested_record.py` | Unpack a nested record (line 148) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_tuples-as-records-not-just-immutable-lists.py` | Tuples as records, not just "immutable lists" (line 57) | runs on its own |
| `examples/02_unpacking-reading-a-record.py` | Unpacking: reading a record (line 92) | may use names from earlier examples |
| `examples/03_looping-over-a-list-of-records.py` | Looping over a list of records (line 118) | may use names from earlier examples |
| `examples/04_a-tuple-can-contain-a-mutable-object.py` | A tuple can contain a mutable object (line 189) | raises an error on purpose |
| `examples/05_a-tuple-can-contain-a-mutable-object.py` | A tuple can contain a mutable object (line 206) | raises an error on purpose |
| `examples/06_a-tuple-can-contain-a-mutable-object.py` | A tuple can contain a mutable object (line 236) | may use names from earlier examples |
| `examples/07_why-immutability-is-a-feature.py` | Why immutability is a feature (line 274) | may use names from earlier examples |
| `examples/08_why-immutability-is-a-feature.py` | Why immutability is a feature (line 289) | may use names from earlier examples |
| `examples/09_why-immutability-is-a-feature.py` | Why immutability is a feature (line 303) | may use names from earlier examples |
| `examples/10_the-problem-namedtuple-solves.py` | The problem `namedtuple` solves (line 326) | may use names from earlier examples |
| `examples/11_creating-and-reading-a-namedtuple.py` | Creating and reading a `namedtuple` (line 350) | may use names from earlier examples |
| `examples/12_creating-and-reading-a-namedtuple.py` | Creating and reading a `namedtuple` (line 365) | may use names from earlier examples |
| `examples/13_creating-and-reading-a-namedtuple.py` | Creating and reading a `namedtuple` (line 382) | may use names from earlier examples |
| `examples/14_creating-and-reading-a-namedtuple.py` | Creating and reading a `namedtuple` (line 401) | may use names from earlier examples |
| `examples/15_make-build-one-from-an-existing-sequence.py` | `_make` — build one from an existing sequence (line 431) | may use names from earlier examples |
| `examples/16_asdict-turn-it-into-a-dictionary.py` | `_asdict` — turn it into a dictionary (line 446) | may use names from earlier examples |
| `examples/17_replace-a-modified-copy.py` | `_replace` — a modified copy (line 459) | may use names from earlier examples |
| `examples/18_replace-a-modified-copy.py` | `_replace` — a modified copy (line 477) | may use names from earlier examples |
| `examples/19_fields-the-field-names-themselves.py` | `_fields` — the field names themselves (line 509) | may use names from earlier examples |
| `examples/20_default-values.py` | Default values (line 533) | may use names from earlier examples |
| `examples/21_default-values.py` | Default values (line 556) | may use names from earlier examples |
| `examples/22_docstrings.py` | Docstrings (line 598) | may use names from earlier examples |
| `examples/23_combining-fields-into-a-new-type.py` | Combining fields into a new type (line 624) | may use names from earlier examples |
| `examples/24_returning-multiple-values-properly.py` | Returning multiple values properly (line 649) | may use names from earlier examples |
| `examples/25_a-fixed-record-instead-of-a-dictionary.py` | A fixed record instead of a dictionary (line 680) | may use names from earlier examples |
| `examples/26_try-it-yourself.py` | Try it yourself (line 736) | may use names from earlier examples |
| `examples/27_try-it-yourself.py` | Try it yourself (line 767) | may use names from earlier examples |
