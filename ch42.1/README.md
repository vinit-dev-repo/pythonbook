# 42.1 - Serialization, pickle, JSON and Custom Encoding

The code of the chapter **42.1 - Serialization, pickle, JSON and Custom Encoding** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What serialization is and why programs use it
- `pickle`: Python's own format, what it can do, and its serious security warning
- How Python values change when you save and load JSON
- How to teach JSON to save your own classes, with custom encoders

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_pickle-python-s-native-format.py` | pickle: Python's native format (line 57) | runs on its own |
| `examples/02_pickle-python-s-native-format.py` | pickle: Python's native format (line 78) | may use names from earlier examples |
| `examples/03_what-pickle-can-save-that-json-cannot.py` | pickle: Python's native format › What pickle can save that JSON cannot (line 106) | may use names from earlier examples |
| `examples/04_the-type-mapping-what-survives-the-trip-and-what.py` | JSON: the universal text format › The type mapping: what survives the trip, and what doesn't (line 199) | may use names from earlier examples |
| `examples/05_shared-objects-and-cycles-are-not-just-equal-val.py` | JSON: the universal text format › Shared objects and cycles are not just equal values (line 227) | runs on its own |
| `examples/06_choose-duplicate-key-and-non-finite-number-polic.py` | JSON: the universal text format › Choose duplicate-key and non-finite-number policies (line 271) | runs on its own |
| `examples/07_dumps-loads-and-dump-load.py` | JSON: the universal text format › dumps/loads and dump/load (line 339) | may use names from earlier examples |
| `examples/08_dumps-loads-and-dump-load.py` | JSON: the universal text format › dumps/loads and dump/load (line 357) | may use names from earlier examples |
| `examples/09_formatting-options.py` | JSON: the universal text format › Formatting options (line 378) | may use names from earlier examples |
| `examples/10_custom-encoding-teaching-json-about-your-own-typ.py` | Custom encoding: teaching JSON about your own types (line 420) | raises an error on purpose |
| `examples/11_fix-1-the-default-function.py` | Custom encoding: teaching JSON about your own types › Fix 1: the `default=` function (line 452) | may use names from earlier examples |
| `examples/12_fix-2-subclassing-jsonencoder.py` | Custom encoding: teaching JSON about your own types › Fix 2: subclassing JSONEncoder (line 477) | may use names from earlier examples |
| `examples/13_encoding-your-own-classes-add-a-type-marker.py` | Custom encoding: teaching JSON about your own types › Encoding your own classes: add a type marker (line 503) | may use names from earlier examples |
| `examples/14_try-it-yourself.py` | Try it yourself (line 558) | runs on its own |
