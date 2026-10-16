# 42 - Serialization

The code of the chapter **42 - Serialization** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What serialization is and why programs use it
- `pickle` — Python's own format, what it can do, and its serious security warning
- How Python values change when you save and load JSON
- How to teach JSON to save your own classes, with custom encoders and decoders
- How to use a schema to reject invalid JSON before using it
- How to navigate nested data and follow stored references through properties
- A quick tour of YAML and typed validation with `pydantic`
- Reading and writing XML while keeping text, bytes and nested content distinct

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `person_boundary.py` | JSON schema, in plain words › Validate before constructing a Person (line 744) |  |
| `test_person_boundary.py` | JSON schema, in plain words › Validate before constructing a Person (line 803) |  |
| `exercise_person_boundary.py` | JSON schema, in plain words › Practice: keep the previous accepted Person (line 938) |  |
| `shape_result_lab.py` | Build a small recursive shape validator › First return a result from every level (line 1007) |  |
| `shape_exception_lab.py` | Build a small recursive shape validator › Then let an exception travel through the calls (line 1064) |  |
| `data_view_lab.py` | Explore nested data through attributes (line 1151) |  |
| `linked_archive.py` | Related serialization tools › Properties can follow stored references (line 1300) |  |
| `linked_archive_demo.py` | Related serialization tools › Properties can follow stored references (line 1394) |  |
| `workshop_json_lab.py` | Preserve typed records inside a document › A tagged format with a fixed registry (line 1683) |  |
| `workshop_schema_lab.py` | Preserve typed records inside a document › Let schemas carry the type information instead (line 1780) |  |
| `xml_records.py` | Parse XML with its structure intact (line 1850) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_pickle-python-s-native-format.py` | pickle — Python's native format (line 59) | runs on its own |
| `examples/02_pickle-python-s-native-format.py` | pickle — Python's native format (line 81) | may use names from earlier examples |
| `examples/03_what-pickle-can-save-that-json-cannot.py` | pickle — Python's native format › What pickle can save that JSON cannot (line 111) | may use names from earlier examples |
| `examples/04_the-type-mapping-what-survives-the-trip-and-what.py` | JSON — the universal text format › The type mapping: what survives the trip, and what doesn't (line 209) | may use names from earlier examples |
| `examples/05_shared-objects-and-cycles-are-not-just-equal-val.py` | JSON — the universal text format › Shared objects and cycles are not just equal values (line 239) | runs on its own |
| `examples/06_choose-duplicate-key-and-non-finite-number-polic.py` | JSON — the universal text format › Choose duplicate-key and non-finite-number policies (line 285) | runs on its own |
| `examples/07_dumps-loads-and-dump-load.py` | JSON — the universal text format › dumps/loads and dump/load (line 356) | may use names from earlier examples |
| `examples/08_dumps-loads-and-dump-load.py` | JSON — the universal text format › dumps/loads and dump/load (line 374) | may use names from earlier examples |
| `examples/09_formatting-options.py` | JSON — the universal text format › Formatting options (line 397) | may use names from earlier examples |
| `examples/10_custom-encoding-teaching-json-about-your-own-typ.py` | Custom encoding: teaching JSON about your own types (line 436) | raises an error on purpose |
| `examples/11_fix-1-the-default-function.py` | Custom encoding: teaching JSON about your own types › Fix 1: the `default=` function (line 470) | may use names from earlier examples |
| `examples/12_fix-2-subclassing-jsonencoder.py` | Custom encoding: teaching JSON about your own types › Fix 2: subclassing JSONEncoder (line 497) | may use names from earlier examples |
| `examples/13_encoding-your-own-classes-add-a-type-marker.py` | Custom encoding: teaching JSON about your own types › Encoding your own classes: add a type marker (line 525) | may use names from earlier examples |
| `examples/14_object-hook.py` | Custom decoding: rebuilding your own objects › object_hook (line 565) | may use names from earlier examples |
| `examples/15_fix-2-mirrored-subclassing-jsondecoder.py` | Custom decoding: rebuilding your own objects › Fix 2, mirrored: subclassing JSONDecoder (line 604) | may use names from earlier examples |
| `examples/16_the-round-trip-a-person-survives-dumps-and-loads.py` | Custom decoding: rebuilding your own objects › The round-trip: a Person survives dumps and loads intact (line 647) | may use names from earlier examples |
| `examples/17_json-schema-in-plain-words.py` | JSON schema, in plain words (line 699) | may use names from earlier examples |
| `examples/18_shelve-a-dictionary-that-lives-on-disk.py` | Related serialization tools › `shelve` — a dictionary that lives on disk (line 1249) | may use names from earlier examples |
| `examples/19_pyyaml-human-friendly-configuration-files.py` | Related serialization tools › PyYAML — human-friendly configuration files (line 1474) | may use names from earlier examples |
| `examples/20_pyyaml-human-friendly-configuration-files.py` | Related serialization tools › PyYAML — human-friendly configuration files (line 1498) | may use names from earlier examples |
| `examples/21_marshmallow-schemas-that-serialize-and-validate.py` | Related serialization tools › Marshmallow — schemas that serialize AND validate (line 1533) | may use names from earlier examples |
| `examples/22_serpy-a-historical-one-way-serializer.py` | Related serialization tools › Serpy — a historical one-way serializer (line 1572) | may use names from earlier examples |
| `examples/23_serpy-a-historical-one-way-serializer.py` | Related serialization tools › Serpy — a historical one-way serializer (line 1603) | may use names from earlier examples |
| `examples/24_serpy-a-historical-one-way-serializer.py` | Related serialization tools › Serpy — a historical one-way serializer (line 1625) | runs on its own |
| `examples/25_try-it-yourself.py` | Try it yourself (line 1942) | may use names from earlier examples |
